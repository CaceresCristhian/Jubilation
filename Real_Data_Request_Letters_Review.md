# Real-Data Transition Review
## Wealth, Migration & Retirement Sustainability in Germany (2025–2070)

**Purpose:** Consolidated review of the research project and the five current data-request letters before submission.

**Reviewed documents**
1. FDZ-RV / VSKT application
2. Deutsche Bundesbank RDSC / PHF application
3. IAB-FDZ / IAB-BAMF-SOEP application
4. Destatis FDZ / Mikrozensus + EVS application
5. Supervisor endorsement letter
6. Previous project README / project plan / master data-request strategy

> **Important:** This is a review checklist, not a replacement application. Exact dataset names, waves, variable names, access modes and confidentiality rules must be confirmed against the current official documentation of each FDZ before submission.

---

# 1. Overall assessment

The project has a strong overall research architecture, but the applications should **not yet be submitted unchanged**.

The central transition is:

**Previous approach**
> Synthetic/calibrated microdata → econometric estimates → microsimulation → policy results

**Target approach**
> Real authorized microdata → harmonized empirical estimates/distributions → calibrated microsimulation → robustness/scenario analysis → policy results

The synthetic pipeline should therefore remain as a **development, testing and reproducibility sandbox**, while real-data estimates become the empirical basis of the final study.

## Complementary role of the four data sources

| Source | Main empirical role |
|---|---|
| FDZ-RV / VSKT | Statutory pension histories and contribution trajectories |
| Bundesbank PHF | Household wealth, assets, liabilities, housing and private financial buffers |
| IAB-BAMF-SOEP / related IAB products | Migration, labour-market integration, education, recognition, language and employment |
| Destatis Mikrozensus | Population structure, migration, labour-market and socioeconomic calibration |
| Destatis EVS | Income/consumption/household-budget calibration where required |

The final study should be described as a **multi-source statistical integration/calibration framework**, not as a direct record linkage of all four datasets.

---

# 2. Project-level review

## 2.1 Separate the research questions

The project currently combines pension accumulation, labour-market integration, deskilling, private wealth, migration/refugee differences, gender, social assistance, fertility and long-run simulation.

Use a hierarchy:

### Primary empirical question

> How do migration timing, labour-market trajectories and socioeconomic characteristics affect statutory pension accumulation and private retirement resources among different migrant and native populations in Germany?

### Secondary questions

- How do labour-market integration and qualification recognition relate to earnings trajectories?
- How do migration duration and household characteristics relate to private wealth accumulation?
- How large are gender differences in pension and wealth outcomes?
- Which groups face elevated old-age income inadequacy under specified assumptions?

### Simulation questions

- What happens under alternative labour-market integration paths?
- What happens under alternative savings/wealth paths?
- How do demographic/fertility assumptions affect retirement outcomes?
- How sensitive are results to pension, wage, inflation and return assumptions?

This separation will make the data requests much easier to justify.

---

# 3. Harmonise the five population groups

Current groups:

1. German native
2. General migrant
3. General refugee
4. Ukrainian war refugee (2022+)
5. Ukrainian pre-2022 migrant

Convert these into explicit operational classification rules using, where available:

- country of birth
- citizenship
- year of immigration
- migration reason/status
- asylum/refugee status
- Ukraine-specific identification
- first vs second generation
- residence duration
- observation year

## Critical point

Do not assume the same five groups can be identified identically in every dataset.

- VSKT should primarily provide the pension/insurance component.
- IAB is much more appropriate for detailed refugee and migration trajectories.
- PHF can contribute migration characteristics but is primarily a household-finance survey.
- Mikrozensus can support population definitions and calibration.

Create a **dataset-specific cohort classification layer**.

---

# 4. Individual wealth vs household wealth

This is one of the most important methodological issues.

The project's earlier goal emphasizes **individual wealth**, but PHF is fundamentally a household-finance survey. The current PHF letter requests household net wealth, assets, liabilities and household income. fileciteturn1file1L84-L130

Do not claim:

> PHF provides individual wealth directly.

Instead state:

> PHF provides household-level wealth and financial information that will be used to estimate household wealth distributions and, where methodologically defensible, translate these resources into individual lifecycle scenarios.

Distinguish:

- individual income
- household income
- individual pension entitlement
- household financial wealth
- housing wealth
- household liabilities
- individual vs household retirement adequacy

Any individual allocation rule must be documented and sensitivity-tested.

---

# 5. Do not directly merge the four sources by default

Create a formal harmonisation layer.

Recommended structure:

```text
01_sources/
02_raw_data/
    drv/
    bundesbank/
    iab/
    destatis/

03_documentation/
    drv_dictionary/
    bundesbank_dictionary/
    iab_dictionary/
    destatis_dictionary/

04_harmonized/
    person_level/
    household_level/
    migration/
    labour/
    wealth/
    pension/
    demographics/

05_processed/
    analytical_samples/
    longitudinal/
    model_ready/

06_synthetic_data/
    development/
    validation/

07_engine/
08_models_econometrics/
09_tests/
10_outputs/
11_reproducibility/
12_publication/
```

---

# 6. Create one master variable specification

Before finalising the letters, create:

| Research concept | Required variable | Dataset | Level | Time | Essential? | Purpose |
|---|---|---|---|---|---|---|
| Age | age/year of birth | multiple | person | longitudinal/cross-section | Yes | lifecycle |
| Migration | year of arrival | IAB/Destatis/PHF where available | person | — | Yes | residence duration |
| Pension | contribution periods | VSKT | person | longitudinal | Yes | GRV |
| Pension | earnings/EP | VSKT | person | longitudinal | Yes | pension accumulation |
| Wealth | net wealth | PHF | household | waves | Yes | wealth |
| Labour | employment/wage | IAB/Destatis | person | longitudinal/cross-section | Yes | wage path |
| Education | education/qualification | IAB/Destatis/PHF | person/household | — | Yes | human capital |
| Fertility | children/birth information | Destatis/IAB | person/household | — | Yes/conditional | demographic scenarios |
| Consumption | expenditure | EVS | household | waves | Optional | retirement budget |
| Remittances | transfers abroad | IAB/PHF if available | person/household | longitudinal/waves | Optional | savings capacity |

This specification should drive all four applications.

---

# 7. Letter 1 — FDZ-RV / VSKT

## Strengths

The application correctly identifies VSKT as the main source for contribution histories, insurance periods, pension points, child-care periods and pension-relevant earnings. fileciteturn1file0L68-L83

The variable list is directionally appropriate and includes demographics, nationality, insurance biography, EPs, child-care periods and earnings. fileciteturn1file0L85-L122

## CRITICAL fixes

### 7.1 Replace uncertain “VSKT 2020–2024”

The current letter says:

> “Neueste verfügbare Welle (VSKT 2020-2024).” fileciteturn1file0L19-L25

Do not submit this until the exact currently available VSKT product/version is confirmed.

### 7.2 Clarify access mode

The letter asks for SUF and “alternatively/additionally” JoSuA.

Do not assume JoSuA is simply an alternative for more detailed variables. Ask which product/access route provides the required variables.

### 7.3 Do not assume VSKT identifies all refugee groups

Use VSKT primarily for pension/insurance outcomes. Refugee classification should preferably be supported by IAB/Destatis.

### 7.4 Remove causal wording

The application asks what portion of the pension gap is caused by missing recognition/deskilling. fileciteturn1file0L55-L67

VSKT alone does not establish that causal mechanism.

Use association/prediction wording unless a separate causal design is available.

### 7.5 Verify all pension variables

Separate:

- insurance periods
- contribution periods
- credited periods
- earnings
- pension points
- retirement status/outcome
- child-care periods
- waiting-period indicators

Use official variable names/codes from the current codebook.

### 7.6 Do not hard-code a permanent basic-security threshold

The application uses approximately €1,113/month. fileciteturn1file0L65-L67

Treat the threshold as a time-specific model parameter depending on legal/economic year and household circumstances.

### 7.7 Treat 2026 pension parameters as model inputs

The letter currently embeds 2026 pension parameters. fileciteturn1file0L75-L81

Keep these in the model specification, not as fixed assumptions in the data request.

---

# 8. Letter 2 — Deutsche Bundesbank RDSC / PHF

## Strengths

The PHF application has a strong wealth focus and requests net wealth, financial assets, capital-market assets, real estate, liabilities, private pensions and income. fileciteturn1file1L84-L130

## CRITICAL fixes

### 8.1 Correct household/person terminology

The letter currently describes the requested PHF data as “Household level and Person level.” fileciteturn1file1L21-L25

Make clear that the wealth outcomes are primarily household-level, while person-level characteristics may be used to analyse household wealth.

### 8.2 Verify the access route

The letter requests “Remote Data Execution via JoSuA.”

Confirm the current RDSC access terminology and only request an access mechanism actually offered for PHF.

### 8.3 Verify variable codes

Codes such as `DA3001`, `DA2101` and `DA2105` should be checked against the current PHF codebook before submission.

If not confirmed, use official documented variable names rather than guessed codes.

### 8.4 Justify all five waves

The request for Waves 1–5 is potentially useful, but explain:

- Wave 5 = latest wealth structure
- earlier waves = temporal/longitudinal context
- multiple waves = wealth accumulation/transition analysis

Do not imply a perfectly balanced individual panel.

### 8.5 Be cautious with refugee identification

Do not assume PHF alone can cleanly identify every refugee cohort. Use IAB/Destatis where necessary.

### 8.6 Remove the unsupported “>80%” claim

The application states that migrant/refugee households have cash/deposit concentration above 80%. fileciteturn1file1L50-L63

Unless directly supported by prior literature, remove the numerical threshold.

### 8.7 Separate portfolio composition from investment returns

Observed wealth and portfolio composition do not automatically provide realised investment returns.

Distinguish:

- portfolio composition
- wealth levels
- wealth changes
- assumed/modelled asset returns

---

# 9. Letter 3 — IAB-FDZ / IAB-BAMF-SOEP

## Strengths

This is the key source for migration trajectories, refugee status, labour-market integration, education, recognition, language, earnings, remittances and family characteristics. fileciteturn1file2L83-L124

## CRITICAL fixes

### 9.1 Verify exact dataset products

The letter combines IAB-BAMF-SOEP M3–M5 with IAB-SOEP M1/M2.

Identify each exact product separately:

- exact dataset name
- version
- waves
- access mode
- scientific necessity

### 9.2 Confirm Ukrainian coverage

The letter specifically requests Ukrainian refugees under §24 AufenthG.

Verify that the requested product/sample provides the required coverage and identification.

### 9.3 Remove automatic causal language

The application says it will isolate a causal wage penalty from recognition/language.

Unless a valid causal design exists, use:

> estimate the association between qualification recognition, language proficiency and earnings using appropriate controls and longitudinal methods.

### 9.4 Heckman Two-Step needs identification

Before committing to Heckman, define a defensible exclusion restriction.

If none exists, treat Heckman as an optional robustness model rather than the default method.

### 9.5 Avoid promising “random/fixed effects” before inspecting the data

Use:

> longitudinal/panel econometric models, including fixed-effects specifications where supported by the data.

### 9.6 Verify variable names

Names such as `zuzug`, `zuzugsjahr`, `anerkennung_status`, `labgro` and `ueberweis_betrag` must be checked against the actual codebook.

Do not submit invented variable codes.

### 9.7 Make remittances optional

Remittances are useful but secondary to the central pension/wealth question. Mark them as optional unless they directly feed a defined model component.

---

# 10. Letter 4 — Destatis FDZ / Mikrozensus + EVS

## Strengths

The application correctly positions Destatis as a population-calibration and socioeconomic reference source. The requested domains cover migration, education, employment, income, household structure, housing and retirement income. fileciteturn1file3L48-L87

## CRITICAL fixes

### 10.1 Separate Mikrozensus and EVS roles

**Mikrozensus**
- population structure
- migration
- labour market
- education
- household characteristics
- income distributions where available

**EVS**
- household income
- consumption/expenditure
- household budgets
- relevant wealth/financial information where available

### 10.2 Do not request EVS without a defined use

Explain exactly what EVS contributes that Mikrozensus cannot.

### 10.3 Verify requested years

The application requests Mikrozensus 2019–2023 and EVS 2018/2023. fileciteturn1file3L18-L24

Confirm current availability and justify each year.

### 10.4 Soften “exact residence duration”

Say:

> duration of residence derived from available migration/arrival-year variables

unless the exact required variable is confirmed.

### 10.5 Do not equate observed rent with SGB XII KdU

Separate:

- observed rent
- housing expenditure
- modelled eligible housing costs
- legal SGB XII parameters

### 10.6 Position pension variables as validation

VSKT should remain the primary source for detailed pension histories. Destatis retirement-income variables are better used for external validation/calibration.

---

# 11. Letter 5 — Supervisor endorsement

## Strengths

The supervisor letter confirms enrolment, supervision, project title, scientific necessity and data-security commitments. fileciteturn1file4L19-L48

## CRITICAL fixes

### 11.1 Remove the generic JoSuA statement

The letter endorses “SUF bzw. Fernrechenzugang (JoSuA)” across the institutions. fileciteturn1file4L43-L48

Because access mechanisms differ, the endorsement should support the scientific need for the datasets without promising a particular technology for every institution.

### 11.2 Harmonise completion dates

Some applications specify December 2027, while the supervisor letter says Wintersemester 2026/2027. Align them.

### 11.3 Use institution-approved compliance wording

Do not make the university/supervisor promise more than the university is formally authorized to guarantee.

### 11.4 Complete signature/date/stamp

Ensure the final signed version contains the required date, supervisor signature and institutional stamp if applicable.

---

# 12. Cross-letter consistency

All documents should use identical:

- researcher name
- student ID
- university
- degree programme
- supervisor
- project title
- expected completion date
- terminology

## Population terminology

Choose definitions explicitly rather than mixing:

- migrant / immigrant / Zuwanderer
- refugee / Geflüchtete
- native / native-born reference population

Avoid “native German” unless the actual classification is defined.

---

# 13. Existing synthetic results

The current project contains quantitative results based on synthetic/calibrated data, including wage/deskilling effects, wealth gaps, pension outcomes, replacement rates and required savings.

These should not be presented as empirical findings from German microdata.

Use labels such as:

- **Synthetic baseline result**
- **Calibrated model result**
- **Preliminary simulation result**

After real-data analysis:

- **Real-data estimate**
- **Observed distribution**
- **Empirically calibrated parameter**

---

# 14. Keep the synthetic pipeline

Do not delete the synthetic data system.

Use it for:

### Software development
- pension calculations
- wealth accumulation
- microsimulation
- visualisation
- reproducibility

### Method validation
Test whether known parameters can be recovered.

### Confidential-data preparation
Develop and test the pipeline before confidential data are accessed.

Recommended:

```text
06_synthetic_data/
    generation/
    benchmark/
    unit_tests/
    sensitivity_tests/
```

---

# 15. Recommended microsimulation modules

## A — Demographics
Age, sex, migration, mortality, fertility, migration flows.

## B — Labour market
Employment, unemployment, wages, hours, occupation, education, recognition, residence duration.

## C — Pension
Contribution periods, pension points, earnings, retirement age, pension parameters.

## D — Private wealth
Financial wealth, housing wealth, debt, savings, private pension, asset allocation.

## E — Taxes/transfers
Taxes, social contributions, Grundsicherung and applicable allowances.

## F — Retirement adequacy
Pension income, private wealth, total retirement resources, replacement ratio, poverty/basic-security risk, required savings and wealth depletion.

---

# 16. Fertility/demographic component

Separate:

### Micro level
Effects of children on:
- employment
- earnings
- pension credits
- savings
- household structure

### Macro level
Effects of fertility on:
- population ageing
- worker/retiree ratios
- contribution base
- pension-system sustainability

Do not imply that one dataset identifies the complete demographic mechanism.

---

# 17. Econometric review

## Mincer models

Keep Mincer-type earnings models, but distinguish:

- descriptive association
- predictive model
- causal model

Controls alone do not make a coefficient causal.

## Wealth models

IHS is a reasonable candidate for skewed wealth with zero/negative observations.

Consider robustness using:

- two-part models
- quantile methods
- extensive/intensive margin analysis
- distributional statistics

## Oaxaca-Blinder

Useful for decomposition, but the unexplained component should not automatically be interpreted as discrimination or causality.

## Heckman

Use only when:

- the selection mechanism is appropriate
- the exclusion restriction is defensible
- assumptions are discussed/tested

## Panel models

Use fixed effects where repeated observations and sufficient within-unit variation exist. Do not promise a panel estimator before inspecting the actual product.

---

# 18. Recommended data-flow

```text
                  DESTATS
           population calibration
                      │
                      ▼
IAB ───────► HARMONISATION ◄────── PHF
migration      LAYER              wealth
labour                             
                      ▲
                      │
                   VSKT
                 pensions
                      │
                      ▼
             EMPIRICAL ESTIMATION
                      │
                      ▼
              MICROSIMULATION
                  2025–2070
                      │
                      ▼
             SCENARIOS / POLICY
```

---

# 19. What each dataset should NOT be responsible for

| Dataset | Do not make it responsible for |
|---|---|
| VSKT | Detailed refugee/labour-market causality |
| PHF | Individual pension-account histories |
| IAB-BAMF-SOEP | Complete household wealth measurement |
| Mikrozensus | Detailed pension-account histories |
| EVS | Detailed administrative pension histories |

This separation strengthens the methodology.

---

# 20. Data harmonisation crosswalk

Create a formal crosswalk:

| Concept | VSKT | IAB | PHF | Mikrozensus | EVS |
|---|---|---|---|---|---|
| Age | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sex | ✓ | ✓ | ✓ | ✓ | ✓ |
| Migration | limited/verify | ✓ | ✓/verify | ✓ | ✓/verify |
| Refugee status | limited/verify | ✓ | verify | verify | verify |
| Employment | ✓/limited | ✓ | ✓ | ✓ | ✓ |
| Earnings | ✓ pension-relevant | ✓ | ✓ | ✓ | ✓ |
| Pension history | ✓ | limited | limited | limited | limited |
| Wealth | limited | limited | ✓ | limited | partial/verify |
| Household | limited | ✓ | ✓ | ✓ | ✓ |
| Fertility/children | ✓/verify | ✓ | ✓ | ✓ | ✓ |

Replace “verify” with exact codebook availability before final submission.

---

# 21. Data-request priority

## Tier 1 — Essential

**FDZ-RV:** pension histories and contribution trajectories.

**IAB:** migration/labour trajectories, refugee analysis, wages, education/recognition.

**PHF:** private wealth, financial assets, housing wealth and liabilities.

**Destatis:** population calibration and representativeness.

## Tier 2 — Highly useful

- EVS
- additional IAB linked products
- richer longitudinal products where scientifically justified

## Tier 3 — Optional

- remittance-specific variables
- very detailed geographic variables
- variables not directly feeding an empirical model

---

# 22. Biggest issues before submission

## CRITICAL

1. Replace uncertain VSKT “2020–2024” wording with an actual product/version.
2. Verify every dataset name and wave.
3. Verify every variable code.
4. Remove generic JoSuA claims unless the relevant institution confirms the route.
5. Correct PHF household-vs-individual terminology.
6. Remove or soften unsupported causal claims.
7. Remove fixed empirical-looking thresholds that are not established.
8. Align project completion dates.
9. Define the five population groups operationally.
10. State clearly that datasets are not automatically directly linked at person level.
11. Distinguish empirical estimates from synthetic/calibrated results.
12. Make each dataset's specific scientific role explicit.

---

# 23. Recommended changes by letter

| Letter | Priority | Main changes |
|---|---|---|
| FDZ-RV | 🔴 Critical | Exact VSKT product, access mode, migration limitations, pension variables, causal wording |
| Bundesbank PHF | 🔴 Critical | Household/person distinction, exact PHF codes, access route, wealth interpretation |
| IAB | 🔴 Critical | Exact products, refugee coverage, causal wording, variable-code verification, Heckman identification |
| Destatis | 🟠 High | Separate Mikrozensus/EVS roles, years, variable availability, housing/rent interpretation |
| Supervisor | 🟠 High | Remove generic JoSuA endorsement, align dates, use institution-approved compliance language |

---

# 24. Recommended final positioning

The strongest version of the project is:

> **A multi-source empirical microsimulation study of retirement adequacy among migrant and native populations in Germany, combining administrative pension histories, household wealth data, migration/labour-market trajectories and representative population statistics.**

The four main sources answer different questions:

**VSKT** → What pension rights/trajectories are observed?

**IAB** → How do migration and labour-market integration shape earnings and employment?

**PHF** → What private wealth and asset buffers exist?

**Destatis** → How representative are the observed distributions and how should the population be calibrated?

**Microsimulation** → What could these trajectories imply for retirement outcomes under alternative assumptions through 2070?

---

# 25. Recommended next document

Do **not** rewrite all four applications independently first.

Create:

## `DATA_REQUEST_SPECIFICATION.md`

It should contain:

1. Research questions
2. Five population definitions
3. Dataset role
4. Master variable list
5. Required waves
6. Access mode
7. Essential vs optional variables
8. Expected analytical output
9. Harmonisation strategy
10. Confidentiality constraints

Then revise each institutional application from this single specification.

This will prevent contradictions and make the four requests look like components of **one coherent scientific project**.

---

# 26. Submission-readiness checklist

## Project
- [ ] Primary research question fixed
- [ ] Secondary questions fixed
- [ ] Five population definitions operationalised
- [ ] Synthetic results labelled as preliminary
- [ ] Real-data methodology separated from simulation
- [ ] Individual vs household wealth clearly defined
- [ ] Multi-source integration strategy documented

## FDZ-RV
- [ ] Exact VSKT product confirmed
- [ ] Exact wave/version confirmed
- [ ] Variables checked against codebook
- [ ] Refugee-identification claim softened
- [ ] Pension parameters removed from fixed application text
- [ ] Causal claims revised

## Bundesbank
- [ ] PHF household-level nature acknowledged
- [ ] Variable codes verified
- [ ] Waves justified
- [ ] Access route verified
- [ ] Wealth-to-individual allocation methodology planned

## IAB
- [ ] Exact product(s) confirmed
- [ ] M1/M2/M3–M5 necessity justified
- [ ] Ukrainian coverage confirmed
- [ ] Variable codes verified
- [ ] Causal recognition claim revised
- [ ] Heckman identification assessed
- [ ] Remittances marked optional if appropriate

## Destatis
- [ ] Mikrozensus role defined
- [ ] EVS role defined
- [ ] Years justified
- [ ] Variable availability verified
- [ ] Housing-cost terminology corrected
- [ ] Pension data positioned as validation, not primary source

## Supervisor
- [ ] Completion date harmonised
- [ ] Generic JoSuA statement removed/revised
- [ ] Signature/date/stamp completed
- [ ] Institutional wording verified

---

# 27. Bottom line

The project is **well suited to a real-data transition**, but the current letters are still draft data-request documents.

The largest risks are:

- requesting products/variables too specifically without verified codebook support;
- assuming access mechanisms;
- blurring household and individual measurement;
- overstating causal identification;
- implying that all four datasets provide identical population classifications.

The overall data strategy is sound. The next step is to convert it into a single **Data Request Specification**, verify the official products/variables/access routes, and then revise each letter from that specification.
