# Wealth Accumulation, Migration & Retirement Sustainability in Germany (2025–2070)

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Data Tests](https://img.shields.io/badge/data%20tests-passing-brightgreen.svg)](07_tests/test_data_integrity.py)
[![Status](https://img.shields.io/badge/status-active%20development-orange.svg)]()

A dynamic empirical microsimulation framework for assessing individual financial wealth trajectories, statutory pension entitlements (*Gesetzliche Rentenversicherung - SGB VI*), social security safety nets (*Grundsicherung im Alter - SGB XII*), and retirement adequacy across diverse population segments in Germany up to 2070.

---

## 1. Core Comparative Taxonomy

The project conducts a formal multi-group comparative analysis across **5 key target populations**:

1. **German Native Reference (`German_Native`)**: Native-born German citizens with continuous domestic contribution records.
2. **General Migrants (`General_Migrant`)**: 1st generation economic, EU, and third-country labor migrants.
3. **General Refugees (`General_Refugee`)**: Historical international protection cohorts (e.g., 2015/2016 waves from Syria, Afghanistan, Iraq).
4. **Ukrainian War Refugees (`Ukrainian_Refugee_2022plus`)**: Displaced persons arriving after February 2022 under § 24 AufenthG (predominantly female caregivers).
5. **Ukrainian Pre-2022 Migrants (`Ukrainian_Migrant_Pre2022`)**: Ukrainian citizens who arrived prior to 2022 for employment, studies, or family reunification.
*(Plus 2nd generation migrants as a complementary cohort)*

---

## 2. Baseline Empirical Comparison (Working-Age Adults, 25–64)

| Population Segment | Sample ($N$) | Median Age | Mean Years in DE | Median Gross Wage (EUR/yr) | Median Financial Wealth | Median Net Wealth | Stock / ETF Investor % | Homeownership % | Median Pension Points ($EP$) | Est. Statutory Pension at 67 (EUR/mo) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. German Native** | 25,643 | 45 | 44.9 | **€58,355** | **€7,226** | **€21,983** | 31.1% | 41.5% | **30.2 EP** | **€1,273 / mo** |
| **2. General Migrant** | 7,097 | 42 | 18.1 | **€48,389** | **€3,914** | **€5,298** | 25.9% | 20.7% | **14.0 EP** | **€592 / mo** |
| **3. General Refugee** | 2,481 | 35 | 9.8 | **€39,583** | **€1,781** | **€1,504** | 15.3% | 6.1% | **7.1 EP** | **€299 / mo** |
| **4. Ukrainian Refugee (2022+)** | 1,328 | 39 | 2.6 | **€33,027** | **€632** | **€424** | 14.9% | 5.4% | **1.3 EP** | **€54 / mo** |
| **5. Ukrainian Migrant (Pre-2022)** | 927 | 41 | 13.4 | **€50,031** | **€3,911** | **€4,875** | 32.5% | 19.8% | **12.5 EP** | **€526 / mo** |

---

## 3. Repository Architecture

```
Jubilacion/
|-- 00_admin/                      # Research questions, assumptions, data dictionary
|   |-- data_dictionary.md
|   |-- assumptions_log.csv
|
|-- 01_sources/                    # Source catalog and automated ingestion pipelines
|   |-- source_catalog.csv
|   |-- build_official_datasets.py
|
|-- 02_raw_data/                   # Raw official extracts & SUF files (secure)
|
|-- 03_synthetic_data/             # Harmonized synthetic microdata (N = 50,000)
|   |-- synthetic_individual_microdata.parquet
|   |-- synthetic_individual_microdata_sample1000.csv
|
|-- 04_processed/                  # Cleaned & calibrated institutional series
|   |-- destatis_demographics_16_bvb_2024_2070.csv
|   |-- bundesbank_wealth_distribution_phf_dwa.csv
|   |-- drv_pension_parameters_and_outcomes.csv
|   |-- drv_cohort_pension_realized.csv
|   |-- iab_bamf_migration_refugee_trajectories.csv
|   |-- sgb_xii_grundsicherung_benchmarks.csv
|   |-- macro_cpi_interest_series.csv
|
|-- 05_engine/                     # Simulation modules & actuarial calculators
|   |-- grv_pension_calculator.py
|   |-- sgb_xii_safety_net.py
|   |-- wealth_accumulation.py
|   |-- demographic_projection.py
|   |-- adequacy_evaluator.py
|   |-- simulation_pipeline.py
|
|-- 06_models_econometrics/        # IHS regressions, wage equations & deskilling models
|   |-- ihs_wealth_regressions.py
|   |-- deskilling_wage_regression.py
|
|-- 07_tests/                      # Automated accounting & actuarial test suites
|   |-- test_data_integrity.py
|   |-- test_simulation_engines.py
|
|-- 08_outputs/                    # Tables, reports, figures & interactive dashboards
|   |-- tables/
|   |   |-- baseline_wealth_and_pension_summary.csv
|   |   |-- simulated_retirement_adequacy_summary.csv
|   |   |-- econometric_ihs_wealth_regressions.csv
|   |   |-- econometric_wage_deskilling_regressions.csv
|   |-- reports/
|   |   |-- baseline_summary_report.md
|   |   |-- simulation_adequacy_report.md
|   |   |-- econometric_ihs_wealth_report.md
|   |   |-- econometric_wage_deskilling_report.md
|   |-- figures/
|   |   |-- fig1_5way_retirement_income_and_nrr.png
|   |   |-- fig2_demographic_pressure_2070_oadr.png
|   |   |-- fig3_poverty_risk_and_savings_gap.png
|   |-- dashboards/
|   |   |-- interactive_dashboard.html
|
|-- 09_reproducibility/            # One-click pipeline runner & environment configs
|   |-- run_all.py
|   |-- requirements.txt
|   |-- environment.yml
|
|-- 10_publication/                # IEEE LaTeX manuscript package & BibTeX
|   |-- IEEEtran.cls
|   |-- ieeeaccess.cls
|   |-- German_Retirement_Wealth_Migration_IEEE.tex
|   |-- references.bib
|   |-- figures/
|
|-- README.md                      # Project documentation (this file)
|-- plan_patrimonio_migracion_jubilacion_alemania.txt  # Primary plan (ES)
|-- PLAN_RESEARCH_GERMANY_RETIREMENT_2070.md          # Technical blueprint (EN)
|-- CITATION.cff                   # Academic citation metadata
|-- LICENSE                        # Open source MIT / CC-BY-4.0 license
```

---

## 4. Key Institutional & Methodological Pillars

1. **Statutory Pension Insurance (*SGB VI*)**: Full deterministic legal implementation of the German pension formula ($R_{\text{brutto}} = \sum \text{EP} \times \text{ZF} \times \text{AR} \times \text{RAF}$), the 33-year *Grundrente* supplement (§ 76g), and the demographic Sustainability Factor (*Nachhaltigkeitsfaktor*).
2. **Social Safety Net (*SGB XII, Chapter 4*)**: Means-tested *Grundsicherung im Alter* (€1,113/mo) with €10,000 liquid asset protection (*Schonvermögen*) and § 82a statutory pension exemptions.
3. **Parametric Copula Calibration ($N = 50,000$)**: Preserves exact marginal quantiles ($p_{10}, p_{25}, p_{50}, p_{75}, p_{90}$) and joint covariance structures from Destatis, Bundesbank PHF Wave 4 / DWA 2024, DRV Rentenatlas, and IAB-BAMF-SOEP without privacy infringement (§ 16 BStatG, § 75 SGB X).
4. **Dual-Track Reproducibility**: Enables instant execution on the open synthetic sandbox, while allowing authorized researchers to plug in confidential FDZ-RV / PHF Scientific Use Files (SUF) into `02_raw_data/` for institutional runs.
5. **Econometric Rigor**: Inverse Hyperbolic Sine (**IHS**) transforms for skewed/negative net wealth, and Mincerian wage equations measuring qualification deskilling penalties ($-65.5\%, p < 0.0001$).

---

## 5. Quick Start & Execution

### One-Click Master Pipeline (Runs Everything in ~12 Seconds):
```bash
python 09_reproducibility/run_all.py
```

### Open Interactive Web Dashboard:
Simply open [`08_outputs/dashboards/interactive_dashboard.html`](08_outputs/dashboards/interactive_dashboard.html) in any web browser to explore dynamic charts and use the individual pension calculator.

---

## 6. Primary Documentation References
- **Methodological Blueprint & Equations:** [`PLAN_RESEARCH_GERMANY_RETIREMENT_2070.md`](PLAN_RESEARCH_GERMANY_RETIREMENT_2070.md)
- **Primary Research Plan (Spanish):** [`plan_patrimonio_migracion_jubilacion_alemania.txt`](plan_patrimonio_migracion_jubilacion_alemania.txt)
- **Data Dictionary:** [`00_admin/data_dictionary.md`](00_admin/data_dictionary.md)
- **Assumptions Log:** [`00_admin/assumptions_log.csv`](00_admin/assumptions_log.csv)
- **Source Catalog:** [`01_sources/source_catalog.csv`](01_sources/source_catalog.csv)

---

## 7. Official Data Sources & Academic Provenance

### Primary Institutional Sources:
1. **Statistisches Bundesamt (Destatis)**: *16. koordinierte Bevölkerungsvorausberechnung (16. BVB, 2024–2070)*; *Einkommens- und Verbrauchsstichprobe (EVS)*; *Mikrozensus*. ([destatis.de](https://www.destatis.de))
2. **Deutsche Bundesbank**: *Distributional Wealth Accounts (DWA 2024–2026)*; *Panel on Household Finances (PHF)*; *SDMX Macroeconomic Statistics*. ([bundesbank.de](https://www.bundesbank.de))
3. **Deutsche Rentenversicherung Bund (DRV)**: *Rentenatlas 2024/2025*; *Rentenwertbestimmungsverordnung*; *Forschungsdatenzentrum der Rentenversicherung (FDZ-RV)*. ([deutsche-rentenversicherung.de](https://www.deutsche-rentenversicherung.de))
4. **Institut für Arbeitsmarkt- und Berufsforschung (IAB / BAMF)**: *IAB-BAMF-SOEP Refugee Longitudinal Surveys*; *Ukrainian Integration Monitoring*. ([iab.de](https://iab.de))
5. **Bundesministerium für Arbeit und Soziales (BMAS)**: *SGB VI (Gesetzliche Rente)*; *SGB XII (Grundsicherung im Alter, Bedarfsstufen & KdU)*; *EStG (§ 22, 32a)*. ([bmas.de](https://www.bmas.de))
6. **OECD & European Commission**: *OECD Pensions at a Glance 2023/2025*; *The 2024 Ageing Report*. ([oecd.org/pensions](https://www.oecd.org/pensions/))

---

## 8. Methodological Transparency & AI Disclosure Statement

> **Academic Provenance & Scientific Transparency**:  
> This research framework, econometric regression suite, and dynamic microsimulation platform were designed, engineered, and calibrated by **Antigravity (Google DeepMind)** under the continuous **domain direction, architectural specification, and methodological supervision of the user**.  
> All statutory pension mechanics (SGB VI), social safety net thresholds (SGB XII), tax formulas (EStG), and empirical parameters are strictly derived from official German and European institutional publications. The harmonized microdata ($N = 50,000$) is generated using parametric Copula methods with exact marginal and covariance preservation to guarantee 100% academic reproducibility while respecting survey privacy (SUF regulations).
