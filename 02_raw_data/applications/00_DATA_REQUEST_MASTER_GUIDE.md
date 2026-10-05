# Master Guide: Official Research Data Applications (FDZ)

This directory contains the complete, ready-to-submit official application dossiers to request real individual-level microdata from the four authoritative German Research Data Centres (**Forschungsdatenzentren – FDZ**).

---

## 1. Applicant Profile Summary (Incorporated into all Dossiers)

* **Primary Researcher / Applicant:** Cristhian David Cáceres Mateus
* **Matriculation Number:** `93515346`
* **Degree Program:** Master of Science in Data Science (M.Sc. Data Science)
* **Academic Institution:** University of Europe for Applied Sciences (UE Germany)
* **Campus:** Berlin, Germany
* **Academic Supervisor:** Prof. Dr. Talha Ali Khan, Department of Business
* **Supervisor E-Mail:** talhaali.khan@ue-germany.de
* **Research Project Title:**  
  *English:* Wealth, Migration & Retirement Sustainability in Germany: Dynamic Microsimulation and Econometric Policy Analysis (2025–2070)  
  *German:* Vermögen, Migration und Alterssicherung in Deutschland: Dynamische Mikrosimulation und ökonometrische Politikanalyse (2025–2070)

---

## 2. Overview of Application Documents in this Directory

| Document / Dossier | Target Institution | Target Dataset | Primary Access Mode |
|:---|:---|:---|:---|
| [Master-Spezifikation (Blueprint)](./DATA_REQUEST_SPECIFICATION.md) | **Alle Forschungsdatenzentren (FDZ)** | Übergreifende methodische Spezifikation | Methodisches Referenzdokument |
| [Dossier 01: Rentenversicherung (VSKT)](./01_FDZ_RV_Antrag_Datennutzung_VSKT.md) | **Forschungsdatenzentrum der Rentenversicherung (FDZ-RV)** | **VSKT (Versichertenkonten-Stichprobe)** | Scientific Use File (SUF) / Remote Execution |
| [Dossier 02: Bundesbank (PHF Vermögen)](./02_Bundesbank_RDSC_Application_PHF.md) | **Deutsche Bundesbank (RDSC)** | **PHF (Panel on Household Finances)** | Scientific Use File (SUF) / Remote Execution |
| [Dossier 03: IAB Arbeitsmarkt (Geflüchtete)](./03_IAB_FDZ_Antrag_SUF_Refugees_SOEP.md) | **FDZ des IAB (Institut für Arbeitsmarkt- & Berufsforschung)** | **IAB-BAMF-SOEP Befragung von Geflüchteten** | Scientific Use File (SUF) |
| [Dossier 04: Statistische Ämter (Mikrozensus)](./04_Destatis_FDZ_Antrag_Mikrozensus_EVS.md) | **Forschungsdatenzentren der Statistischen Ämter** | **Mikrozensus & EVS Scientific Use Files** | Scientific Use File (SUF) |
| [Dossier 05: Betreuer-Befürwortung (Prof. Talha)](./05_Betreuerbefuerwortung_Supervisor_Endorsement_Letter.md) | **Alle Forschungsdatenzentren (FDZ)** | Master's Thesis Project Endorsement | Institutional Endorsement Letter |

---

## 3. Step-by-Step Submission Procedures

### Track A: Deutsche Rentenversicherung (FDZ-RV) — Longitudinal Pension Accounts
1. **Portal:** Visit [https://www.fdz-rv.de/](https://www.fdz-rv.de/) -> *Datenzugang* -> *Antrag auf Datennutzung*.
2. **Documents to submit:**
   - Completed [`01_FDZ_RV_Antrag_Datennutzung_VSKT.md`](./01_FDZ_RV_Antrag_Datennutzung_VSKT.md) (can be pasted into their standard PDF form or submitted as project description annex).
   - Signed Supervisor Endorsement ([`05_Betreuerbefuerwortung_Supervisor_Endorsement_Letter.md`](./05_Betreuerbefuerwortung_Supervisor_Endorsement_Letter.md)).
   - Current certificate of enrollment (*Immatrikulationsbescheinigung*).
3. **Contact Email:** `fdz@drv-bund.de`
4. **Typical Processing Time:** 2 to 4 weeks. (Access is free of charge for university research).

### Track B: Deutsche Bundesbank (RDSC) — Household Wealth Panel (PHF)
1. **Portal:** Register on the Bundesbank Research Data and Service Centre portal: [https://www.bundesbank.de/en/service/research-data-and-service-centre](https://www.bundesbank.de/en/service/research-data-and-service-centre).
2. **Documents to submit:**
   - Completed project description based on [`02_Bundesbank_RDSC_Application_PHF.md`](./02_Bundesbank_RDSC_Application_PHF.md).
   - Co-signature / endorsement from Prof. Dr. Talha Ali Khan.
3. **Contact Email:** `researchdata-service@bundesbank.de`
4. **Typical Processing Time:** 3 to 5 weeks.

### Track C: IAB Nürnberg — Refugee Labor Market Integration & Remittances
1. **Portal:** Visit [https://fdz.iab.de/en/](https://fdz.iab.de/en/) -> *Data Access* -> *Application*.
2. **Dataset code:** `IAB-BAMF-SOEP` (SUF).
3. **Documents to submit:**
   - Use the text from [`03_IAB_FDZ_Antrag_SUF_Refugees_SOEP.md`](./03_IAB_FDZ_Antrag_SUF_Refugees_SOEP.md).
   - Countersigned Data Use Agreement (*Nutzungsvertrag*).
4. **Contact Email:** `iab.fdz@iab.de`
5. **Typical Processing Time:** 2 to 3 weeks.

### Track D: Destatis / Statistische Ämter — Microcensus & EVS
1. **Portal:** Visit [https://www.forschungsdatenzentrum.de/en/request](https://www.forschungsdatenzentrum.de/en/request).
2. **Documents to submit:**
   - Project outline from [`04_Destatis_FDZ_Antrag_Mikrozensus_EVS.md`](./04_Destatis_FDZ_Antrag_Mikrozensus_EVS.md).
   - Student ID and University of Europe affiliation proof.
3. **Typical Processing Time:** 2 to 4 weeks.

---

## 4. Once You Receive Your Data
When your application is approved and you download the Scientific Use File (e.g., `vskt2024_suf.dta` or `phf_wave5_suf.csv`):
1. Place the files into the designated subfolder:
   - DRV data -> `02_raw_data/drv_pension_atlas/`
   - Bundesbank data -> `02_raw_data/bundesbank_dwa_phf/`
   - IAB data -> `02_raw_data/iab_bamf_integration/`
2. The project's Dual-Track pipeline will automatically detect the real microdata and execute the models directly on administrative records.
