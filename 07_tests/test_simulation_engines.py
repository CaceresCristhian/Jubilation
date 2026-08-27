"""
Actuarial & Simulation Engine Unit Tests
Verifies mathematical and legal consistency of the pension, safety net, and wealth engines.
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "05_engine")))

from grv_pension_calculator import GRVPensionCalculator
from sgb_xii_safety_net import SGBXIISafetyNet
from wealth_accumulation import WealthAccumulationEngine
from adequacy_evaluator import RetirementAdequacyEvaluator

def test_grv_standard_pension():
    calc = GRVPensionCalculator(aktueller_rentenwert=42.15, durchschnittsentgelt=51944.0, beitragsbemessungsgrenze=101400.0)
    # Standard pensioner with 45 EP at age 67 with children (KV 8.75% + PV 3.6% = 12.35% deduction)
    res_parent = calc.calculate_pension(accumulated_ep=45.0, contribution_years=45.0, retirement_age=67.0, has_children=True)
    assert res_parent["gross_monthly_pension_eur"] == 1896.75
    assert res_parent["kvdr_deduction_eur"] == 165.97
    assert res_parent["pv_deduction_eur"] == 68.28
    assert res_parent["net_monthly_pension_eur"] == 1662.50
    assert res_parent["zugangsfaktor_zf"] == 1.0

    # Childless pensioner (KV 8.75% + PV 4.2% = 12.95% deduction)
    res_childless = calc.calculate_pension(accumulated_ep=45.0, contribution_years=45.0, retirement_age=67.0, has_children=False)
    assert res_childless["pv_deduction_eur"] == 79.66
    assert res_childless["net_monthly_pension_eur"] == 1651.12
    print("  [PASS] Standard GRV Eckrente (45 EP) exactly reconciled: €1,896.75 gross -> €1,662.50 net (parent) / €1,651.12 net (childless).")

def test_grv_early_and_delayed_retirement():
    calc = GRVPensionCalculator()
    # 2 years early (age 65 vs 67) -> -7.2% deduction (ZF = 0.928)
    res_early = calc.calculate_pension(accumulated_ep=40.0, contribution_years=40.0, retirement_age=65.0)
    assert res_early["zugangsfaktor_zf"] == 0.928

    # 1 year late (age 68 vs 67) -> +6.0% bonus (ZF = 1.060)
    res_late = calc.calculate_pension(accumulated_ep=40.0, contribution_years=40.0, retirement_age=68.0)
    assert res_late["zugangsfaktor_zf"] == 1.060
    print("  [PASS] Early retirement deductions (-0.3%/mo) and delayed bonuses (+0.5%/mo) verified.")

def test_sgb_xii_safety_net_activation():
    net = SGBXIISafetyNet(regelbedarf_stufe1=563.0, avg_kdu_housing=550.0, schonvermoegen_single=10000.0)
    
    # Profile A: Low pension (300 EUR/mo), zero assets -> qualifies for top-up to 1,113 EUR
    res_a = net.calculate_benefit(net_pension_income=300.0, other_net_income=0.0, liquid_financial_assets=2000.0)
    assert res_a["eligible_for_sgb_xii"] is True
    assert res_a["disposable_monthly_income_eur"] == 1113.0
    assert res_a["monthly_transfer_eur"] == 813.0

    # Profile B: High liquid assets (15,000 EUR > 10,000 EUR Schonvermögen) -> ineligibility due to excess assets
    res_b = net.calculate_benefit(net_pension_income=300.0, other_net_income=0.0, liquid_financial_assets=15000.0)
    assert res_b["eligible_for_sgb_xii"] is False
    print("  [PASS] SGB XII Grundsicherung means-testing & Schonvermögen (€10k) verified.")

def test_wealth_accumulation_budget_constraint():
    engine = WealthAccumulationEngine(real_return_equity=0.05, real_return_cash=-0.005)
    # 30-year-old earning 45,000 EUR
    res = engine.project_wealth_at_retirement(current_age=30, current_deposits=5000.0, current_investments=10000.0, annual_gross_wage=45000.0)
    assert res["years_accumulated"] == 37
    assert res["projected_financial_wealth_at_67"] > 50000.0
    assert res["safe_monthly_withdrawal_4pct"] > 0
    print("  [PASS] Wealth accumulation and intertemporal portfolio returns verified.")

if __name__ == "__main__":
    print("Running actuarial and simulation engine test suite...")
    test_grv_standard_pension()
    test_grv_early_and_delayed_retirement()
    test_sgb_xii_safety_net_activation()
    test_wealth_accumulation_budget_constraint()
    print("\nALL 4 ACTUARIAL TEST SUITES PASSED PERFECTLY WITH ZERO ERRORS!")
