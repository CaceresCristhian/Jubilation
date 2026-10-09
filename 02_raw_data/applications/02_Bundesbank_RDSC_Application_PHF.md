# Research Data Access Application (Deutsche Bundesbank RDSC)
## Research Data and Service Centre (RDSC)
**Deutsche Bundesbank**  
Wilhelm-Epstein-Straße 14  
60431 Frankfurt am Main, Germany  
E-Mail: researchdata-service@bundesbank.de | Web: https://www.bundesbank.de/rdsc

---

### 1. General Project & Researcher Information

* **Primary Researcher / Applicant:** Cristhian David Cáceres Mateus
* **Matriculation Number:** `93515346`
* **Status:** Academic Researcher / Project Member (M.Sc. Data Science)
* **Academic Institution:** University of Europe for Applied Sciences (UE Germany)
* **Campus Address:** Potsdam Campus (Think Campus, Konrad-Zuse-Ring 11, 14469 Potsdam, Germany)
* **Project Director / Faculty Supervisor:** Prof. Dr. Talha Ali Khan, Department of Business
* **Supervisor E-Mail:** talhaali.khan@ue-germany.de
* **Project Type:** University Scientific Research Project / Institutional Research
* **Requested Access Mode:**  
  *Primary:* **Scientific Use File (SUF)** / Off-site Research Data  
  *Secondary:* **Remote Data Execution** via the Bundesbank RDSC secure submission infrastructure.

---

### 2. Dataset Information

* **Requested Dataset:** **Panel on Household Finances (PHF)**
* **Requested Waves:** Wave 1 (2010/11), Wave 2 (2014), Wave 3 (2017), Wave 4 (2020/21), and Wave 5 (2023, published 2025/2026).
  * *Wave Justification:* Wave 5 provides the most current empirical wealth distribution; Waves 1–4 provide structural comparison across time to estimate wealth accumulation trajectories across cohorts.
* **Data Units:** Household level for asset, liability, and wealth aggregates; Person level for individual demographic, migration, and human capital characteristics.

---

### 3. Project Title and Abstract

* **Project Title:**  
  *Private Wealth Accumulation, Portfolio Composition, and Retirement Buffer Capacity Among Native and Migrant Households in Germany: Evidence from the Bundesbank Panel on Household Finances (PHF)*
* **Working Title:**  
  *Household Wealth Trajectories and Social Safety Net Interactions across Native, Migrant, and Refugee Cohorts (2025–2070)*

#### Abstract:
In light of demographic pressures on Germany's pay-as-you-go public pension pillar (GRV), household private wealth accumulation is increasingly recognized as a vital second pillar for mitigating old-age income poverty. However, empirical wealth gaps between native German households and migrant populations remain pronounced, driven by disparities in initial endowments, labor market trajectories, duration of residence, homeownership rates, and financial asset participation.

This research project investigates the structural determinants of financial and net wealth accumulation across native German households, first-generation labor migrants, and displaced/refugee cohorts using microdata from the Bundesbank Panel on Household Finances (PHF). By estimating Inverse Hyperbolic Sine (IHS) wealth regressions and portfolio selection models, this study quantifies: (1) the magnitude of the unconditional and conditional net wealth gap between native and immigrant households, (2) the rate of economic wealth assimilation per year of German residency, (3) the role of portfolio allocation (liquid cash deposits vs. equity/ETF market participation) in wealth growth, and (4) the capacity of accumulated private assets to fund stylized decumulation withdrawals at statutory retirement (age 67) before triggering means-tested basic social assistance (*Grundsicherung im Alter*, Chapter 4, SGB XII).

---

### 4. Theoretical Background, Research Questions & Hypotheses

#### Research Hypotheses:
* **Hypothesis 1 (Initial Wealth Penalty & Endowments):** First-generation migrant and refugee households enter the German financial system with significantly lower initial net and financial wealth compared to demographically comparable native households, controlling for age and education.
* **Hypothesis 2 (Wealth Assimilation Velocity):** Net wealth accumulates at an increasing concave rate with years of residence in Germany ($\beta_{\text{residence}} > 0, \beta_{\text{residence}^2} < 0$), narrowing the asset gap relative to native households over multi-decade horizons.
* **Hypothesis 3 (Portfolio Heterogeneity & Asset Shares):** Migrant and refugee households exhibit significantly higher portfolio concentration in liquid bank deposits and lower capital market participation (stocks, mutual funds, ETFs) compared to native households, which is hypothesized to lower real portfolio returns net of inflation.
* **Hypothesis 4 (Asset Depletion & SGB XII Means-Testing):** Due to lower financial buffers and lower homeownership rates, a substantially higher proportion of aging migrant households will exhaust their liquid wealth down to statutory exemption thresholds (*Schonvermögen*, § 90 SGB XII), necessitating social safety net top-ups.

---

### 5. Econometric Methodology

1. **Inverse Hyperbolic Sine (IHS) Wealth Regressions:**
   Because net and financial wealth distributions exhibit significant skewness, zero values, and negative entries (indebtedness), we apply the IHS transformation:
   $$\text{IHS}(W_i) = \ln\left(W_i + \sqrt{W_i^2 + 1}\right)$$
   Models are estimated via OLS with heteroskedasticity-consistent robust standard errors (HC1/HC3), clustering at the household level across multiple imputations. Robustness checks include two-part models and quantile regressions.
2. **Covariate Controls:**
   Age, age squared, household size, education (ISCED tertiary/vocational), employment status, gross household income, duration of residence in Germany, country/region of origin, self-employment status, and homeownership dummy.
3. **Decomposition Analysis:**
   Oaxaca-Blinder decomposition of the native-migrant wealth gap into explained endowments (education, income, age) and unexplained structural differences.
4. **Household-to-Individual Allocation & Microsimulation Calibration:**
   To interface household wealth measures with individual pension rights in the dynamic microsimulation, household assets will be modeled across household types (single vs. couple) and allocated to individuals via documented equivalence scales and sharing scenarios, accompanied by explicit sensitivity analysis. Realized capital market returns are modeled parametrically via deterministic scenarios and sensitivity bounds.

---

### 6. Detailed List of Requested PHF Variables

| Domain | Variable Codes / Concept in PHF | Purpose in Research Project |
|:---|:---|:---|
| **Household Identifiers** | `ID`, `WAVE`, `IMPUTATION_NO`, `WEIGHTS` | Panel tracking, multiply-imputed data handling, survey weighting. |
| **Demographics** | Age of reference person, gender, marital status | Lifecycle age-bracket segmentation, gender dimension. |
| **Migration Background** | Born in Germany, year of immigration, country of origin, citizenship | Defining target cohorts: German native, 1st gen migrant, refugee cohort. |
| **Labor & Human Capital** | Employment status, occupation, ISCED education, years of experience | Controlling for human capital and labor market stability. |
| **Net Wealth Components** | Total household net wealth (`DA3001`), total assets, total liabilities | Core dependent variable for wealth gap and assimilation models. |
| **Financial Wealth** | Checking accounts, savings accounts, certificates of deposit (`DA2101`) | Calibrating liquid cash reserves and safety buffers. |
| **Capital Market Assets** | Mutual funds, stocks, bonds, managed investment accounts (`DA2105`) | Quantifying equity market participation and real returns. |
| **Real Estate & Housing** | Homeownership status, primary residence market value, remaining mortgage balance | Evaluating housing equity and shelter cost mitigation in retirement. |
| **Private Pension Assets** | Private pension contracts (Riester, Rürup, occupational *Betriebsrente*) | Analyzing Pillar 2 and Pillar 3 voluntary pension provision. |
| **Debt & Liabilities** | Mortgage debt, consumer loans, overdrafts, total household debt | Accounting identity verification: $\text{Net Wealth} = \text{Assets} - \text{Liabilities}$. |
| **Income & Savings** | Annual gross/net household income, regular monthly savings rate | Income-to-wealth ratios, savings capacity modeling. |

---

### 7. Confidentiality, Data Security & Compliance Statement

In accordance with the Deutsche Bundesbank RDSC Data Access Agreement and European GDPR standards:
1. **Academic Use Only:** Data will be utilized strictly for the scientific academic research project and associated peer-reviewed scientific publications.
2. **Non-Disclosure:** Individual micro-records will never be shared, published, or transmitted to unauthorized parties.
3. **Aggregation Protocol:** All reporting will strictly comply with RDSC output checking guidelines:
   - Minimum cell count $N \ge 5$ (or $N \ge 3$ where authorized).
   - Suppression of individual percentiles or extrema that could risk deductive disclosure.
   - Reporting only regression coefficients, standard errors, test statistics, and smooth distribution curves.
4. **Storage & Erasure:** Microdata files will be stored on an encrypted, access-restricted institutional drive at the University of Europe for Applied Sciences and will be permanently erased upon project termination (scheduled completion: December 2027).

---

### 8. Signatures

**Date and Place:** Potsdam, ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Applicant / Academic Researcher, Student ID: 93515346)

\
____________________________________________________  
**Prof. Dr. Talha Ali Khan**  
(Project Director / Professor, Department of Business, University of Europe for Applied Sciences)
