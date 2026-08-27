"""
Social Safety Net Calculator (Grundsicherung im Alter - SGB XII, 4. Kapitel)
Implements:
- Bedarfsberechnung: Regelbedarf (Stufe 1/2) + Kosten der Unterkunft und Heizung (KdU) + Mehrbedarfe
- Einkommensanrechnung (means-testing)
- Exemption for GRV pensions with 33+ contribution years (§ 82a SGB XII)
- Asset protection limits (Schonvermögen: 10,000 EUR single / 20,000 EUR couple)
"""

class SGBXIISafetyNet:
    def __init__(self,
                 regelbedarf_stufe1: float = 563.0, # 2026 single adult standard rate
                 regelbedarf_stufe2: float = 506.0, # partner in couple
                 avg_kdu_housing: float = 550.0,   # illustrative accommodation & heating benchmark
                 schonvermoegen_single: float = 10000.0,
                 schonvermoegen_couple: float = 20000.0,
                 freibetrag_pension_max_82a: float = 281.50):
        self.rb1 = regelbedarf_stufe1
        self.rb2 = regelbedarf_stufe2
        self.avg_kdu = avg_kdu_housing
        self.schon_single = schonvermoegen_single
        self.schon_couple = schonvermoegen_couple
        self.fb_max = freibetrag_pension_max_82a

    def calculate_benefit(self,
                          net_pension_income: float,
                          other_net_income: float,
                          liquid_financial_assets: float,
                          contribution_years: float = 0.0,
                          is_single: bool = True,
                          actual_kdu: float = None,
                          owns_adequate_home: bool = False) -> dict:
        """
        Calculates eligibility and payout of Grundsicherung im Alter.
        """
        # 1. Total subsistence need (Bedarf)
        regelbedarf = self.rb1 if is_single else self.rb2
        kdu = actual_kdu if actual_kdu is not None else self.avg_kdu
        
        # If owning home, KdU covers heating, maintenance and property levies (approx 45% of rent)
        if owns_adequate_home:
            kdu = kdu * 0.45
            
        total_bedarf = regelbedarf + kdu
        
        # 2. Asset test (Schonvermögen § 90 SGB XII)
        asset_limit = self.schon_single if is_single else self.schon_couple
        excess_assets = max(0.0, liquid_financial_assets - asset_limit)
        
        # If excess liquid assets exist, person is not eligible until depleted
        if excess_assets > 0:
            return {
                "eligible_for_sgb_xii": False,
                "total_bedarf_eur": round(total_bedarf, 2),
                "countable_income_eur": 0.0,
                "monthly_transfer_eur": 0.0,
                "disposable_monthly_income_eur": round(net_pension_income + other_net_income, 2),
                "ineligibility_reason": f"Excess liquid assets ({excess_assets:,.0f} EUR above Schonvermögen limit)"
            }
            
        # 3. Pension Exemption (§ 82a SGB XII Freibetrag für gesetzliche Rente)
        pension_exemption = 0.0
        if contribution_years >= 33.0 and net_pension_income > 0:
            # 100 EUR base + 30% of excess, capped at freibetrag_max
            base_free = min(net_pension_income, 100.0)
            remaining_pension = max(0.0, net_pension_income - 100.0)
            pension_exemption = min(self.fb_max, base_free + 0.30 * remaining_pension)
            
        countable_pension = max(0.0, net_pension_income - pension_exemption)
        countable_income = countable_pension + other_net_income
        
        # 4. Net Transfer
        shortfall = total_bedarf - countable_income
        transfer = max(0.0, shortfall)
        eligible = transfer > 0.0
        
        # Total disposable income = actual pension + other income + transfer
        total_disposable = net_pension_income + other_net_income + transfer
        
        return {
            "eligible_for_sgb_xii": eligible,
            "total_bedarf_eur": round(total_bedarf, 2),
            "regelbedarf_eur": round(regelbedarf, 2),
            "kdu_housing_eur": round(kdu, 2),
            "pension_exemption_82a_eur": round(pension_exemption, 2),
            "countable_income_eur": round(countable_income, 2),
            "monthly_transfer_eur": round(transfer, 2),
            "disposable_monthly_income_eur": round(total_disposable, 2),
            "ineligibility_reason": None if eligible else "Income exceeds Bedarf"
        }
