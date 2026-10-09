# Multi-Source Scientific Data Request Specification
## Wealth, Migration & Retirement Sustainability in Germany (2025–2070)

**Applicant:** Cristhian David Cáceres Mateus (Matriculation No. `93515346`)  
**Project Framework:** Academic Research Project / Institutional Research  
**Academic Institution:** University of Europe for Applied Sciences (UE Germany), Potsdam Campus  
**Faculty Project Director:** Prof. Dr. Talha Ali Khan, Department of Business  
**Project Director E-Mail:** `talhaali.khan@ue-germany.de`  
**Target Completion:** Late 2026/2027 (Archival & Data Destruction: December 2027)

---

## 1. Project Architecture & Multi-Source Integration Strategy

### 1.1 Methodological Positioning
This research platform is designed as a **multi-source statistical integration and calibration framework**, **not** a direct deterministic person-level linkage of administrative files. 

Under German data protection legislation (§ 16 BStatG, § 35 SGB I, § 67 SGB X, and EU GDPR), direct cross-institution micro-linkage across independent federal agencies (DRV, Bundesbank, IAB, Destatis) is legally restricted. Consequently, this study adopts a **calibrated microsimulation architecture**:
1. **Administrative Histories (FDZ-RV):** Empirically calibrate statutory pension accumulation trajectories (Entgeltpunkte, contribution years, childcare credits).
2. **Household Balance Sheets (Bundesbank RDSC):** Empirically calibrate household private wealth distributions, housing equity, and liquid buffer dynamics.
3. **Integration & Wage Trajectories (IAB FDZ):** Empirically estimate employment assimilation curves, language acquisition effects, and credential recognition premiums.
4. **Macro-Demographic & Population Weights (Destatis FDZ):** Calibrate population weights, household structures, and baseline demographic projections.
5. **Microsimulation Engine (2025–2070):** Synthesizes these empirical moment distributions into forward-looking individual lifecycle paths to evaluate old-age income adequacy under alternative policy reforms.

### 1.2 Dual-Track Role of Synthetic Microdata
The pre-existing calibrated synthetic dataset ($N = 50,000$) is preserved as a **development, testing, and open-science reproducibility sandbox**. All preliminary figures derived from synthetic records are explicitly designated as *calibrated baseline simulations*. The real microdata requested from the four FDZs will provide the authoritative empirical parameter estimates for the research project and publications.

---

## 2. Research Questions Hierarchy

### Primary Empirical Question
> **How do migration timing, labor-market trajectories, and socioeconomic characteristics shape statutory pension accumulation (GRV) and private retirement asset buffers among migrant and native-born populations in Germany?**

### Secondary Empirical Sub-Questions
1. **Labor Market & Earnings:** How do years since migration, language proficiency, and qualification recognition relate to gross earnings and annual Entgeltpunkte accumulation?
2. **Wealth & Portfolio Composition:** How do household net wealth, financial asset portfolios, and homeownership vary across migration cohorts, and what is the velocity of private wealth accumulation over residence duration?
3. **Gender Pension Gap:** How do child-rearing pension credits (§ 56 SGB VI) and part-time employment patterns moderate retirement income disparities between women and men across migrant and native groups?
4. **Safety Net Interaction:** What proportion of individuals in each cohort face autonomous pension outcomes below illustrative subsistence adequacy benchmarks, requiring means-tested basic social assistance (*Grundsicherung im Alter*, SGB XII, Chapter 4)?

### Policy Simulation Questions
* How would accelerated qualification recognition (*Fast-Track Anerkennung*) alter lifetime pension points?
* What additional monthly private savings ($S^*$) are required under alternative capital market return scenarios to achieve a 60% net replacement rate?

---

## 3. Operational Cohort Definitions Across Datasets

To ensure statistical rigor, cohort definitions reflect the specific measurement capabilities of each dataset:

| Target Cohort | VSKT (FDZ-RV) | IAB-BAMF-SOEP (IAB) | PHF (Bundesbank) | Mikrozensus (Destatis) |
|:---|:---|:---|:---|:---|
| **1. Native Reference Population** | German nationality at birth, domestic contribution history | Non-migrant German reference sample (SOEP Core) | Born in Germany, German citizenship, native parents | German without migration background (*ohne Migrationshintergrund*) |
| **2. General Migrant (1st Gen)** | Foreign nationality / naturalized, delayed contribution start | Immigrants under economic/family categories (M1/M2) | Foreign-born, foreign citizenship or naturalized | First-generation immigrant with direct migration experience |
| **3. General Refugee** | Identified via country of origin & registration timing | Humanitarian migration / registered asylum seekers (M3/M4) | Country of origin proxy (high-asylum countries) | Migration reason: humanitarian/asylum |
| **4. Ukrainian Displaced (2022+)** | Ukrainian citizenship, first domestic contribution $\ge 2022$ | Ukrainian refugees registered under § 24 AufenthG (M5) | Arrival year $\ge 2022$, Ukrainian nationality | Ukrainian citizenship, arrival year $\ge 2022$ |
| **5. Ukrainian Pre-2022 Migrant** | Ukrainian citizenship, first domestic contribution $< 2022$ | Ukrainian migrants arriving prior to Feb 2022 | Arrival year $< 2022$, Ukrainian nationality | Ukrainian citizenship, arrival year $< 2022$ |

---

## 4. Household vs. Individual Measurement Protocol

* **Household Wealth (PHF):** Wealth is measured and accumulated primarily at the household level. To interface household assets with individual pension entitlements in the microsimulation, household net and financial wealth will be:
  1. Analyzed at the household level across household types (single, couple, with/without children).
  2. Allocated to individuals using standardized OECD-modified equivalence scales and intra-household sharing rules for scenario testing.
* **Individual Pensions (VSKT):** Statutory pension rights are strictly individualized legal entitlements based on personal contribution records.
* **Separation of Realized Returns from Asset Shares:** Survey data capture static portfolio shares (cash, deposits, equities, real estate). Capital market returns are modeled parametrically via deterministic scenarios and sensitivity bounds.

---

## 5. Master Variable Specification

| Concept | Required Variable Domain | Primary Source | Secondary Source | Level | Essential? | Purpose |
|:---|:---|:---|:---|:---|:---|:---|
| **Demographics** | Birth year, gender, marital status | VSKT | Mikrozensus / IAB | Person | **Yes** | Cohort segmentation, life expectancy |
| **Migration** | Nationality, arrival year, country of birth | IAB / Mikrozensus | VSKT (citizenship) | Person | **Yes** | Residence duration calculation |
| **Legal Status** | § 24 AufenthG, asylum status, work permit | IAB-BAMF-SOEP | Mikrozensus | Person | **Yes** | Refugee cohort isolation |
| **Pension Biography** | Contribution months, credited periods, non-contributory times | VSKT | — | Person | **Yes** | Wartezeit (5, 35, 45 yrs) calculation |
| **Pension Points (EP)** | Total EP, EP from earnings, EP from child-rearing (§ 56) | VSKT | — | Person | **Yes** | Primary pension calculation ($R = EP \times ZF \times AR$) |
| **Basic Pension** | Grundrentenzeiten, Grundrenten-EP (§ 76g) | VSKT | — | Person | **Yes** | SGB XII § 82a disregard modeling |
| **Labor & Wages** | Monthly gross/net wages, full/part-time status | IAB / VSKT | Mikrozensus | Person | **Yes** | Mincer wage equations, contribution base |
| **Education & Recognition**| Foreign degree, formal recognition status, deskilling indicator | IAB-BAMF-SOEP | Mikrozensus | Person | **Yes** | Qualification wage penalty estimation |
| **Language** | CEFR proficiency levels (A1 to C2) | IAB-BAMF-SOEP | — | Person | **Yes** | Human capital wage covariate |
| **Net Wealth** | Total household assets, liabilities, net worth | Bundesbank PHF | EVS (partial) | Household | **Yes** | Wealth gap estimation, decumulation |
| **Liquid Buffers** | Bank deposits, cash, savings accounts | Bundesbank PHF | EVS | Household | **Yes** | SGB XII Schonvermögen (€10,000) threshold |
| **Equity Assets** | Stocks, mutual funds, ETFs | Bundesbank PHF | — | Household | **Yes** | Portfolio composition & real return modeling |
| **Housing** | Homeownership dummy, mortgage balance, property value | Bundesbank PHF | Mikrozensus | Household | **Yes** | Shelter cost mitigation in retirement |
| **Private Pension** | Riester, Rürup, occupational pension contracts | Bundesbank PHF | VSKT (partial) | Household/Person| Highly Useful | Multi-pillar retirement modeling |
| **Household Budget** | Housing costs (rent/heating), basic living expenses | Destatis Mikrozensus / EVS | — | Household | Highly Useful | Calibration of illustrative subsistence benchmark |
| **Remittances** | Financial transfers abroad (amount, frequency) | IAB-BAMF-SOEP | — | Household/Person| Optional | Savings capacity constraint adjustment |

---

## 6. Access Modes & Institutional Protocols

1. **FDZ-RV:** Scientific Use File (SUF) of the *Versichertenkontenstichprobe (VSKT)*. Where detailed migration identifiers require higher granularity, remote execution via FDZ-RV standard procedures will be requested.
2. **Bundesbank RDSC:** Scientific Use File (SUF) / Off-site data or Remote Data Execution (RDSC JoSuA/LISS environment) of the *Panel on Household Finances (PHF)*.
3. **IAB FDZ:** Scientific Use File (SUF) of the *IAB-BAMF-SOEP Befragung von Geflüchteten* and *IAB-SOEP Migrationsstichproben*.
4. **Destatis FDZ:** Scientific Use File (SUF) of the *Mikrozensus* (focus: population weighting) and optional *EVS* (focus: consumption/budgets).
