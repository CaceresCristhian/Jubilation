"""
Statutory Pension Insurance Calculator (Gesetzliche Rentenversicherung - SGB VI)
Implements exact German statutory formulas:
- Entgeltpunkte (EP) accumulation
- Access Factor (Zugangsfaktor - ZF) for early/delayed retirement
- Aktueller Rentenwert (AR) with Sustainability Factor (Nachhaltigkeitsfaktor)
- Grundrente Supplement (§ 76g SGB VI)
- Net Pension after KVdR (Health) and PV (Long-Term Care) deductions
"""

import numpy as np

class GRVPensionCalculator:
    def __init__(self,
                 aktueller_rentenwert: float = 42.52, # Official statutory pension value (post-July 2026)
                 durchschnittsentgelt: float = 51944.0,
                 beitragsbemessungsgrenze: float = 101400.0,
                 kvdr_rate: float = 0.0875, # 7.3% base + 1.45% (half of 2.9% official avg Zusatzbeitrag)
                 pv_rate_with_children: float = 0.0360, # 2026 baseline long-term care rate
                 pv_rate_childless: float = 0.0420):     # 2026 childless surcharge rate
        self.ar = aktueller_rentenwert
        self.durchschnittsentgelt = durchschnittsentgelt
        self.bbg = beitragsbemessungsgrenze
        self.kvdr_rate = kvdr_rate
        self.pv_rate_children = pv_rate_with_children
        self.pv_rate_childless = pv_rate_childless

    def calculate_annual_ep(self, annual_gross_wage: float) -> float:
        """Computes annual Entgeltpunkte based on wage relative to national average."""
        capped_wage = min(annual_gross_wage, self.bbg)
        if capped_wage <= 0:
            return 0.0
        return capped_wage / self.durchschnittsentgelt

    def calculate_zugangsfaktor(self, retirement_age: float, standard_age: float = 67.0) -> float:
        """
        Computes Zugangsfaktor (ZF):
        - Early retirement: -0.3% per month early (max 14.4%)
        - Delayed retirement: +0.5% per month late
        """
        months_diff = (retirement_age - standard_age) * 12.0
        if months_diff < 0:
            deduction = min(0.144, abs(months_diff) * 0.003)
            return max(0.856, 1.0 - deduction)
        elif months_diff > 0:
            bonus = months_diff * 0.005
            return 1.0 + bonus
        return 1.0

    def calculate_grundrente_supplement(self,
                                       contribution_years: float,
                                       accumulated_ep: float,
                                       other_income_monthly: float = 0.0) -> float:
        """
        Calculates Grundrente supplement under § 76g SGB VI:
        - Requires at least 33 years of Grundrentenzeiten.
        - Full supplement at 35+ years.
        - Increases average EP for low earners up to ~0.8 EP/yr max, with 12.5% flat deduction.
        """
        if contribution_years < 33.0 or accumulated_ep <= 0:
            return 0.0
        
        avg_ep_yr = accumulated_ep / contribution_years
        if avg_ep_yr >= 0.8 or avg_ep_yr < 0.3:
            return 0.0
        
        # Scaling factor between 33 and 35 years
        scale = min(1.0, (contribution_years - 33.0) / 2.0) if contribution_years < 35.0 else 1.0
        
        # Target up to 0.8 EP per year for max 35 years
        qualifying_years = min(35.0, contribution_years)
        ep_uplift = (0.8 - avg_ep_yr) * qualifying_years * 0.875 * scale
        
        # Income testing (simplified BMAS thresholds: ~1,375 EUR single exemption)
        if other_income_monthly > 1375.0:
            excess = other_income_monthly - 1375.0
            ep_deduction = (excess * 0.60 * 12.0) / (self.ar * 12.0)
            ep_uplift = max(0.0, ep_uplift - ep_deduction)
            
        return max(0.0, ep_uplift)

    def calculate_pension(self,
                          accumulated_ep: float,
                          contribution_years: float,
                          retirement_age: float = 67.0,
                          has_children: bool = True,
                          other_monthly_income: float = 0.0,
                          apply_grundrente: bool = True) -> dict:
        """
        Calculates full gross and net monthly pension payout.
        """
        zf = self.calculate_zugangsfaktor(retirement_age)
        
        grundrente_ep = 0.0
        if apply_grundrente:
            grundrente_ep = self.calculate_grundrente_supplement(contribution_years, accumulated_ep, other_monthly_income)
            
        total_ep = accumulated_ep + grundrente_ep
        gross_monthly_pension = total_ep * zf * self.ar * 1.0 # RAF = 1.0 for Altersrente
        
        # KVdR and PV Deductions (rounded to cents per statutory payroll standard)
        pv_rate = self.pv_rate_children if has_children else self.pv_rate_childless
        kvdr_deduction = round(gross_monthly_pension * self.kvdr_rate, 2)
        pv_deduction = round(gross_monthly_pension * pv_rate, 2)
        
        net_monthly_pension_before_tax = round(gross_monthly_pension - kvdr_deduction - pv_deduction, 2)
        
        return {
            "accumulated_ep": round(accumulated_ep, 3),
            "grundrente_supplement_ep": round(grundrente_ep, 3),
            "total_ep": round(total_ep, 3),
            "zugangsfaktor_zf": round(zf, 4),
            "gross_monthly_pension_eur": round(gross_monthly_pension, 2),
            "kvdr_deduction_eur": kvdr_deduction,
            "pv_deduction_eur": pv_deduction,
            "net_monthly_pension_eur": net_monthly_pension_before_tax
        }
