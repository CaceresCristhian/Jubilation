"""
Automated Data Integrity and Accounting Identity Tests
for German Retirement, Wealth, and Migration Datasets.
"""

import os
import numpy as np
import pandas as pd

def test_processed_files_exist():
    required_files = [
        "04_processed/destatis_demographics_16_bvb_2024_2070.csv",
        "04_processed/bundesbank_wealth_distribution_phf_dwa.csv",
        "04_processed/drv_pension_parameters_and_outcomes.csv",
        "04_processed/drv_cohort_pension_realized.csv",
        "04_processed/iab_bamf_migration_refugee_trajectories.csv",
        "04_processed/sgb_xii_grundsicherung_benchmarks.csv",
        "04_processed/macro_cpi_interest_series.csv",
        "03_synthetic_data/synthetic_individual_microdata.parquet",
        "01_sources/source_catalog.csv",
        "00_admin/assumptions_log.csv"
    ]
    for rf in required_files:
        assert os.path.exists(rf), f"Missing required dataset: {rf}"
    print("  [PASS] All 10 required dataset and governance files exist.")

def test_demographic_bounds():
    df = pd.read_csv("04_processed/destatis_demographics_16_bvb_2024_2070.csv")
    assert len(df) > 0
    assert df["total_population_millions"].min() > 65.0
    assert df["total_population_millions"].max() < 100.0
    assert df["old_age_dependency_ratio_oadr_pct"].min() >= 30.0
    assert df["old_age_dependency_ratio_oadr_pct"].max() <= 70.0
    print("  [PASS] Demographic projection ranges (16. BVB) match official bounds.")

def test_wealth_accounting_identity_synthetic():
    df = pd.read_parquet("03_synthetic_data/synthetic_individual_microdata.parquet")
    assert len(df) == 50000
    
    # Financial Wealth = Deposit + Investment
    fin_calc = df["deposit_assets_eur"] + df["investment_assets_eur"]
    assert np.allclose(df["financial_wealth_eur"], fin_calc, atol=0.01)

    # Net Wealth = Financial + Housing - Debt
    net_calc = df["financial_wealth_eur"] + df["housing_real_estate_eur"] - df["total_debt_eur"]
    assert np.allclose(df["net_wealth_eur"], net_calc, atol=0.01)

    # Required population cohorts present
    cohorts = set(df["population_group"].unique())
    expected = {"German_Native", "General_Migrant", "General_Refugee", "Ukrainian_Refugee_2022plus", "Ukrainian_Migrant_Pre2022", "Migrant_2ndGen"}
    assert cohorts == expected
    print("  [PASS] Synthetic microdata (N=50,000) satisfies all financial accounting identities across all 6 cohorts.")

def test_pension_parameters():
    df = pd.read_csv("04_processed/drv_pension_parameters_and_outcomes.csv")
    assert df["aktueller_rentenwert_eur"].iloc[-1] > 40.0
    assert df["beitragssatz_pct"].iloc[-1] == 18.6
    print("  [PASS] DRV statutory pension parameters correctly calibrated.")

if __name__ == "__main__":
    print("Running automated data integrity and accounting verification...")
    test_processed_files_exist()
    test_demographic_bounds()
    test_wealth_accounting_identity_synthetic()
    test_pension_parameters()
    print("\nALL DATA INTEGRITY AND ACCOUNTING TESTS PASSED WITH ZERO ERRORS!")
