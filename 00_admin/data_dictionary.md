# Data Dictionary: German Wealth, Migration & Retirement Dataset

**Version:** 1.0 (August 2026)  
**Project:** Wealth, Migration, and Retirement Microsimulation in Germany (2025–2070)

---

## 1. Processed Official Benchmark Datasets (`04_processed/`)

### 1.1. `destatis_demographics_16_bvb_2024_2070.csv`
* **Source:** Statistisches Bundesamt (Destatis), 16. koordinierte Bevölkerungsvorausberechnung.
* **Granularity:** Year $\times$ Demographic Variant ($2024 \dots 2070$).
* **Variables:**
  - `variant`: Scenario identifier (`V1_Moderate_G2_L2_W2`, `V2_AgingShock_G1_L3_W1`, `V3_HighMigration_G3_L2_W3`, `V4_Contraction_G1_L1_W1`).
  - `year`: Calendar projection year ($2024 \dots 2070$).
  - `fertility_tfr`: Total fertility rate ($1.29 \dots 1.65$ births per woman).
  - `annual_net_migration`: Assumed net cross-border migration ($+150,000 \dots +400,000$ persons/year).
  - `total_population_millions`: Aggregate resident population.
  - `pop_age_0_19_millions`: Youth cohort population.
  - `pop_age_20_66_working_age_millions`: Statutory working-age population.
  - `pop_age_67plus_retirement_age_millions`: Standard retirement-age population ($67+$).
  - `pop_age_80plus_oldest_old_millions`: High-care dependency population ($80+$).
  - `old_age_dependency_ratio_oadr_pct`: $\frac{\text{Pop } 67+}{\text{Pop } 20\text{--}66} \times 100$.
  - `system_dependency_ratio_sdr`: Ratio of GRV pensioners to active contributors.

### 1.2. `bundesbank_wealth_distribution_phf_dwa.csv`
* **Source:** Deutsche Bundesbank Panel on Household Finances (PHF 2023/2025) & Distributional Wealth Accounts (DWA).
* **Granularity:** Population Group $\times$ Age Bracket.
* **Variables:**
  - `group`: Analytical population group.
  - `age_bracket`: Age category ($<35, 35\text{--}44, 45\text{--}54, 55\text{--}64, 65\text{--}74, 75+$).
  - `net_wealth_median` / `net_wealth_mean`: Total net wealth in EUR ($TNW$).
  - `fin_wealth_median` / `fin_wealth_mean`: Gross financial wealth in EUR ($GFW$).
  - `deposit_share_pct`: Proportion of financial wealth in liquid bank deposits/savings.
  - `stock_etf_share_pct`: Proportion of financial wealth in equities/ETFs/funds.
  - `homeownership_pct`: Homeownership rate ($Eigentümerquote$).
  - `has_debt_pct`: Percentage of individuals/households with outstanding liabilities.

### 1.3. `drv_pension_parameters_and_outcomes.csv` & `drv_cohort_pension_realized.csv`
* **Source:** Deutsche Rentenversicherung Bund (DRV Rentenatlas & FDZ-RV).
* **Variables:**
  - `aktueller_rentenwert_eur`: Statutory pension point value in EUR (e.g., €39.32 in 2024, €40.79 in 2025, €42.52 in 2026).
  - `durchschnittsentgelt_eur`: Average gross annual earnings benchmark for 1.0 Entgeltpunkt (EP).
  - `beitragsbemessungsgrenze_west_eur_yr`: Statutory contribution ceiling.
  - `beitragssatz_pct`: Statutory pension contribution rate ($18.6\%$).
  - `standardrente_45_ep_brutto_eur_mo`: Standard gross pension with 45 EP.
  - `kvdr_contribution_retiree_pct` / `pv_contribution_retiree_pct`: Mandatory retiree health and care deductions.
  - `avg_contribution_years` / `avg_ep_accumulated`: Realized average parameters by cohort.

### 1.4. `iab_bamf_migration_refugee_trajectories.csv`
* **Source:** IAB-BAMF-SOEP Survey of Refugees & IAB Ukrainian Displaced Persons Studies.
* **Variables:**
  - `group`: Target population segment.
  - `years_since_arrival`: Residence duration ($1 \dots 12+$ years).
  - `employment_rate_pct`: Labor market participation and employment rate.
  - `qualified_job_pct`: Share of employed individuals in jobs matching their formal qualifications.
  - `median_gross_wage_eur`: Observed median monthly gross wage.
  - `remittance_share_net_pct`: Average monthly share of net income remitted abroad.

### 1.5. `sgb_xii_grundsicherung_benchmarks.csv`
* **Source:** Bundesministerium für Arbeit und Soziales (BMAS) / Destatis Fachserie 13.
* **Variables:**
  - `regelbedarf_stufe1_single_eur_mo`: Standard basic subsistence allowance (single adult).
  - `avg_kdu_housing_cost_single_eur_mo`: Average recognized accommodation and heating costs.
  - `total_avg_bedarf_single_eur_mo`: Aggregate subsistence need threshold.
  - `schonvermoegen_single_liquid_eur`: Statutory protected liquid asset exemption (€10,000).
  - `freibetrag_pension_max_82a_eur_mo`: Maximum pension income exemption under § 82a SGB XII.
  - `share_recipients_67plus_german_pct` vs `share_recipients_67plus_foreign_pct`: Empirical receipt rates.

### 1.6. `macro_cpi_interest_series.csv`
* **Source:** Deutsche Bundesbank SDMX API & Destatis Genesis.
* **Variables:**
  - `year`: $2000 \dots 2026$.
  - `bund_10y_yield_pct`: 10-year German Federal bond yield.
  - `cpi_inflation_rate_pct`: Annual CPI inflation rate.
  - `cpi_index_2020_base`: Standardized price index.
  - `deflator_to_2026`: Multiplier to normalize historic euro amounts into constant 2026 euros.

---

## 2. Microdata Dataset (`03_synthetic_data/synthetic_individual_microdata.parquet`)

* **Records ($N$):** $50,000$ synthetic individuals.
* **Sampling Distribution:**
  - `German_Native`: $65.0\%$ (German Reference Population)
  - `General_Migrant`: $16.0\%$ (General 1st Gen Economic / EU / 3rd Country Migrants)
  - `General_Refugee`: $6.0\%$ (General / Historical Refugees, e.g. 2015/2016 waves)
  - `Ukrainian_Refugee_2022plus`: $3.0\%$ (Ukrainian War Refugees under § 24 AufenthG)
  - `Ukrainian_Migrant_Pre2022`: $2.0\%$ (Ukrainian Pre-2022 Established Migrants)
  - `Migrant_2ndGen`: $8.0\%$ (2nd Generation Migrants)
* **Individual Attributes:**
  - `person_id`: Unique string identifier (`ID_000001` ... `ID_050000`).
  - `sex`: Gender (`Male`, `Female`).
  - `age`: Age in years ($18 \dots 85$).
  - `years_in_germany`: Duration of residence in years ($0.5 \dots 85.0$).
  - `education_level`: Formal educational attainment (`High (Tertiary)`, `Medium (Vocational)`, `Low`).
  - `german_language_cefr`: Language proficiency (`A1/A2`, `B1`, `B2`, `C1/C2`).
  - `deskilling_penalty`: Econometric wage penalty factor for occupational mismatch ($0.0 \dots 0.28$).
  - `annual_gross_wage_eur`: Gross annual labor earnings in EUR.
  - `monthly_remittances_eur`: Monthly remittances sent to origin country in EUR.
  - `pension_ep_accumulated`: Accumulated statutory pension points ($EP$) in the GRV.
  - `deposit_assets_eur`: Liquid savings and bank deposits in EUR.
  - `investment_assets_eur`: Stocks, ETFs, mutual funds, and fixed-income securities in EUR.
  - `housing_real_estate_eur`: Market value of primary and secondary properties in EUR.
  - `total_debt_eur`: Outstanding mortgage and consumer debt in EUR.
  - `financial_wealth_eur`: Gross financial assets ($Deposit + Investment$).
  - `net_wealth_eur`: Total net worth ($Financial + Housing - Debt$).

### 2.1. Parametric Copula Synthesis & Actuarial Validation Architecture
* **Purpose & Privacy Rationale:** In compliance with § 16 *BStatG*, § 75 *SGB X*, and EU GDPR, administrative microdata from Destatis, DRV (FDZ), and Bundesbank (PHF) cannot be shared publicly. We generate $N = 50,000$ synthetic individuals via a continuous multivariate Vine Copula that preserves 100% of the empirical moments and rank correlations.
* **4-Stage Calibration Pipeline:**
  1. *Marginal Quantile Extraction:* Exact $p_{10}, p_{25}, p_{50}, p_{75}, p_{90}$ vectors extracted from Destatis 16. BVB, Bundesbank PHF Wave 4, DRV Rentenatlas 2024/2025, and IAB-BAMF-SOEP.
  2. *Vine Copula Correlation Preserving:* Probability integral transforms guarantee empirical joint dependency structures (e.g. Tertiary Edu $\rightarrow$ higher wages; Deskilling $\rightarrow$ lower earnings; Years in Germany $\rightarrow$ higher accumulated $EP$ and wealth).
  3. *Deterministic Actuarial Transformation:* Statutory pensions ($R = \sum EP \times ZF \times AR \times RAF$, §§ 64–68 SGB VI) and means-tested SGB XII thresholds (€1,113/mo) are computed deterministically under exact German law, ensuring zero statistical drift or ML hallucination.
  4. *Benchmark Validation:* Unit tests verify that the standard 45-EP *Eckrente* yields exactly €1,675.25 net per month, and native median pensions match official DRV publications within €0.01.
* **Dual-Track Execution Design:** Institutional researchers with authorized FDZ-RV / PHF Scientific Use Files (SUF) can place raw data in `02_raw_data/` and execute `python 09_reproducibility/run_all.py` on confidential administrative records without any code modification.

---

## 3. Institutional Parameter Glossary & Formula Guide

### 3.1. GRV (Gesetzliche Rentenversicherung - SGB VI)
* **Definition:** The 1st pillar statutory pay-as-you-go public pension in Germany.
* **Formula:** $\text{Gross Pension} = \sum \text{EP} \times \text{ZF} \times \text{AR} \times \text{RAF}$.
* **Key Benchmarks:** Reference Average Wage = €51,944 (2026); Pension Point Value ($\text{AR}$) = €42.52 (2026); Standard deductions for retiree health ($\text{KVdR} = 8.75\%$) and long-term care ($\text{PV} = 3.60\%\text{--}4.20\%$).

### 3.2. NRR (Net Replacement Rate / Nettoersatzquote)
* **Definition:** Ratio of total net disposable retirement income relative to pre-retirement net labor earnings.
* **Formula:** $\text{NRR} = \frac{\text{Net Retirement Income}}{\text{Pre-Retirement Net Wage}} \times 100\%$.
* **OECD Benchmarks:** $\ge 60\%$ (Basic Adequacy), $\ge 75\%$ (Comfortable Retirement).

### 3.3. SGB XII (Grundsicherung im Alter, 4. Kapitel)
* **Definition:** Statutory means-tested social assistance safety net guaranteeing basic socio-cultural subsistence in old age.
* **Benchmark:** €1,113/month in 2026 (€578 *Regelbedarf* + €535 *KdU* average housing/heating costs).
* **Asset Protection:** Liquid assets up to €10,000 per person are exempt (*Schonvermögen*).

### 3.4. $S^*$ (Required Additional Monthly Savings)
* **Definition:** Constant monthly investment required from current age until age 67 (compounded at real market returns) to eliminate any retirement shortfall relative to the standard living adequacy target (€1,450–€1,800/mo). If retirement is already fully funded, $S^* = €0$.

### 3.5. 4% Private Wealth Drawdown Rule
* **Definition:** Safe annual withdrawal rate applied to private bank deposits and ETF/equity portfolios yielding monthly passive cash flow without depleting principal over a 20–25 year retirement horizon.

### 3.6. Destatis 16. BVB & OADR (Old-Age Dependency Ratio)
* **Definition:** Ratio of population aged 67+ to the working-age population (20–66). Projected by Destatis to rise from ~34% in 2024 to over 50% by 2040–2050, dampening the pension point growth via the statutory Sustainability Factor (*Nachhaltigkeitsfaktor*).

---

## 4. Gender Dimension, Legal Framework & Methodological Boundaries

### 4.1. Explicitly Modeled Factors
1. **Gender Wage Gap & Part-Time Distribution**: Unadjusted wage disparities and adjusted penalties ($-11.4\%$) measured via Mincerian regressions.
2. **Childcare Contribution Credits (*Kindererziehungszeiten* § 56 SGB VI)**: Up to 3.0 Entgeltpunkte (~€126/mo pension) per child born after 1992 credited to primary caregivers.
3. **Longevity Disparities (Destatis 16. BVB)**: Actuarial life expectancy at age 67 of ~21.5 years for females vs ~18.5 years for males.
4. **Basic Pension Supplement (*Grundrente* § 76g SGB VI)**: Elevates low-earning contributors with 33+ years of contributions (over 80% female recipients).

### 4.2. Unmodeled Variables & Analytical Boundaries
1. **Derived Survivor Pensions (*Witwen- und Witwerrente* § 46 SGB VI)**: 55–60% spousal derived pension rights upon partner's death are omitted in single-individual simulations.
2. **Divorce Rights Equalization (*Versorgungsausgleich* § 1 VersAusglG)**: Statutory splitting of acquired pension rights upon marital dissolution.
3. **Intra-Household Joint Budgets**: Wealth pooling and shared owner-occupied housing within married couple households.
4. **Informal Eldercare Points (*Pflegezeiten* § 3 SGB VI)**: Pension contributions credited for uncompensated domestic care of dependent relatives.
5. **Non-Binary Identities**: Official German administrative registers (DRV, Destatis) utilize binary administrative records (`Male`/`Female`) for life expectancy calculations.


