"""
Dynamic Wealth Accumulation & Portfolio Engine
Models:
- Intertemporal lifecycle asset growth from current age (t_0) to retirement age (t_R)
- Income taxation (progressive German tax formula § 32a EStG) and social security deductions
- Consumption, housing rent/mortgage, and remittances outflows
- Portfolio split (liquid deposits vs diversified equity/ETF index)
- Capital gains tax (Abgeltungsteuer 25% + SolZ + Sparer-Pauschbetrag)
"""

import numpy as np

class WealthAccumulationEngine:
    def __init__(self,
                 real_return_equity: float = 0.050,  # 5.0% real annualized return
                 real_return_cash: float = -0.005,   # -0.5% real return on cash deposits
                 abgeltungsteuer_rate: float = 0.26375, # 25% + 5.5% SolZ
                 sparer_pauschbetrag: float = 1000.0,
                 mgmt_fee_etf: float = 0.0020):       # 0.20% TER
        self.r_eq = real_return_equity
        self.r_cash = real_return_cash
        self.tax_rate = abgeltungsteuer_rate
        self.pauschbetrag = sparer_pauschbetrag
        self.fee_etf = mgmt_fee_etf

    def estimate_net_wage_income(self, gross_wage_annual: float, is_single: bool = True) -> float:
        """
        Approximates net annual labor income after German progressive income tax (§ 32a EStG)
        and employee social security contributions (~20.5%).
        """
        if gross_wage_annual <= 0:
            return 0.0
            
        # Social security contributions (approx 20.5% for employee share)
        social_sec = gross_wage_annual * 0.205
        
        # Taxable income approx (Grundfreibetrag ~11,784 EUR in 2024/2026)
        taxable_base = max(0.0, gross_wage_annual - social_sec - 1230.0) # Arbeitnehmerpauschbetrag
        
        # Simplified German progressive tax curve
        if taxable_base <= 11784.0:
            tax = 0.0
        elif taxable_base <= 17005.0:
            y = (taxable_base - 11784.0) / 10000.0
            tax = (995.21 * y + 1400.0) * y
        elif taxable_base <= 66760.0:
            z = (taxable_base - 17005.0) / 10000.0
            tax = (208.85 * z + 2397.0) * z + 1015.51
        elif taxable_base <= 277825.0:
            tax = 0.42 * taxable_base - 10632.63
        else:
            tax = 0.45 * taxable_base - 18967.38
            
        net_income = gross_wage_annual - social_sec - tax
        return max(0.0, net_income)

    def project_wealth_at_retirement(self,
                                     current_age: int,
                                     current_deposits: float,
                                     current_investments: float,
                                     annual_gross_wage: float,
                                     monthly_remittances: float = 0.0,
                                     savings_rate_net: float = 0.12,
                                     equity_investment_share: float = 0.50,
                                     retirement_age: int = 67) -> dict:
        """
        Projects liquid deposits and equity/ETF investments to retirement age.
        """
        years_to_retire = max(0, retirement_age - current_age)
        
        deposits = float(current_deposits)
        investments = float(current_investments)
        
        net_wage_annual = self.estimate_net_wage_income(annual_gross_wage)
        annual_remittances = monthly_remittances * 12.0
        
        # Net annual investable savings after remittances and essential living
        disposable_after_remit = max(0.0, net_wage_annual - annual_remittances)
        annual_savings = disposable_after_remit * savings_rate_net
        
        dep_history = [deposits]
        inv_history = [investments]
        
        for yr in range(years_to_retire):
            # Split new annual savings
            savings_to_inv = annual_savings * equity_investment_share
            savings_to_cash = annual_savings * (1.0 - equity_investment_share)
            
            # Cash growth (net real)
            deposits = deposits * (1.0 + self.r_cash) + savings_to_cash
            
            # Investment growth (net of fees and capital gains tax above Pauschbetrag)
            gross_gain = investments * (self.r_eq - self.fee_etf)
            taxable_gain = max(0.0, gross_gain - self.pauschbetrag)
            net_gain = gross_gain - (taxable_gain * self.tax_rate)
            
            investments = investments + net_gain + savings_to_inv
            
            dep_history.append(deposits)
            inv_history.append(investments)
            
        total_financial_wealth = deposits + investments
        
        return {
            "years_accumulated": years_to_retire,
            "projected_deposits_at_67": round(deposits, 2),
            "projected_investments_at_67": round(investments, 2),
            "projected_financial_wealth_at_67": round(total_financial_wealth, 2),
            "annual_net_savings_stream": round(annual_savings, 2),
            "safe_monthly_withdrawal_4pct": round((total_financial_wealth * 0.04) / 12.0, 2)
        }
