"""
Retirement Adequacy and Income Gap Evaluator
Implements:
- Net Replacement Rate (NRR) computation
- Multi-tier adequacy threshold evaluation (Poverty avoidance, Basic adequacy 60%, Comfortable 75%)
- Retirement Income Gap (RIG)
- Required Additional Monthly Savings (S*) formula
"""

import numpy as np

class RetirementAdequacyEvaluator:
    def __init__(self,
                 target_replacement_rate_basic: float = 0.60,
                 target_replacement_rate_comfortable: float = 0.75,
                 poverty_threshold_monthly: float = 1113.0): # SGB XII Bedarf 2026
        self.target_basic = target_replacement_rate_basic
        self.target_comf = target_replacement_rate_comfortable
        self.poverty_line = poverty_threshold_monthly

    def calculate_required_monthly_savings(self,
                                           monthly_income_gap: float,
                                           years_to_retire: int,
                                           expected_retirement_duration_years: int = 20,
                                           real_pre_return: float = 0.045,
                                           real_post_return: float = 0.020) -> float:
        """
        Computes required additional monthly savings (S*) to fund an income gap throughout retirement:
        S* = RIG * a_R(longevity, r_post) / s_n(r_pre)
        """
        if monthly_income_gap <= 0 or years_to_retire <= 0:
            return 0.0
            
        r_m_post = real_post_return / 12.0
        n_months_ret = expected_retirement_duration_years * 12
        
        # Present value factor of retirement annuity at retirement age
        if r_m_post > 0:
            pv_annuity = (1.0 - (1.0 + r_m_post) ** (-n_months_ret)) / r_m_post
        else:
            pv_annuity = float(n_months_ret)
            
        capital_needed_at_67 = monthly_income_gap * pv_annuity
        
        # Future value accumulation factor during working years
        r_m_pre = real_pre_return / 12.0
        n_months_acc = years_to_retire * 12
        
        if r_m_pre > 0:
            fv_annuity = (((1.0 + r_m_pre) ** n_months_acc) - 1.0) / r_m_pre
        else:
            fv_annuity = float(n_months_acc)
            
        s_star_monthly = capital_needed_at_67 / fv_annuity
        return round(s_star_monthly, 2)

    def evaluate_profile_adequacy(self,
                                  pre_retirement_net_monthly: float,
                                  pension_net_monthly: float,
                                  private_wealth_drawdown_monthly: float,
                                  sgb_xii_topup_monthly: float,
                                  years_to_retire: int) -> dict:
        """
        Evaluates full adequacy metrics for an individual profile.
        """
        total_monthly_retirement_income = pension_net_monthly + private_wealth_drawdown_monthly + sgb_xii_topup_monthly
        
        nrr = (total_monthly_retirement_income / pre_retirement_net_monthly) if pre_retirement_net_monthly > 0 else 1.0
        
        # Standard adequacy target capped at official benchmark (€1,800/mo) and bounded by poverty line
        target_income_basic = max(self.poverty_line, min(1800.0, pre_retirement_net_monthly * self.target_basic))
        target_income_comfortable = max(self.poverty_line * 1.25, min(2400.0, pre_retirement_net_monthly * self.target_comf))
        
        # Income gap relative to basic adequacy (without relying on social assistance)
        autonomous_retirement_income = pension_net_monthly + private_wealth_drawdown_monthly
        gap_basic = max(0.0, target_income_basic - autonomous_retirement_income)
        gap_comfortable = max(0.0, target_income_comfortable - autonomous_retirement_income)
        
        # Required additional monthly savings to close basic gap
        s_star_basic = self.calculate_required_monthly_savings(gap_basic, years_to_retire)
        s_star_comfortable = self.calculate_required_monthly_savings(gap_comfortable, years_to_retire)
        
        return {
            "total_monthly_retirement_income_eur": round(total_monthly_retirement_income, 2),
            "autonomous_retirement_income_eur": round(autonomous_retirement_income, 2),
            "net_replacement_rate_nrr": round(nrr, 4),
            "is_above_poverty_line": total_monthly_retirement_income >= self.poverty_line,
            "achieves_basic_adequacy_60pct": nrr >= self.target_basic,
            "achieves_comfortable_adequacy_75pct": nrr >= self.target_comf,
            "relies_on_sgb_xii_safety_net": sgb_xii_topup_monthly > 0,
            "monthly_income_gap_basic_eur": round(gap_basic, 2),
            "monthly_income_gap_comfortable_eur": round(gap_comfortable, 2),
            "required_additional_monthly_savings_basic_eur": s_star_basic,
            "required_additional_monthly_savings_comfortable_eur": s_star_comfortable
        }
