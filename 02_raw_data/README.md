# Raw Data Ingestion & Scientific Use Files (SUF) Access Guide

This directory holds official raw microdata and macro time-series extracts from the Research Data Centres (Forschungsdatenzentren - FDZ) of the Federal Statistical Office (Destatis), Deutsche Bundesbank, Deutsche Rentenversicherung Bund (DRV), and the Institute for Employment Research (IAB).

---

## 1. Directory Structure

- `02_raw_data/destatis_16_bvb/`: Destatis 16. koordinierte Bevölkerungsvorausberechnung (Genesis-Online DB Table 12421).
- `02_raw_data/bundesbank_dwa_phf/`: Bundesbank Distributional Wealth Accounts (DWA) & Panel on Household Finances (PHF Wave 4/5).
- `02_raw_data/drv_pension_atlas/`: DRV Rentenbestand und Rentenzugang official microdata tables (FDZ-RV SUF VSKT).
- `02_raw_data/iab_bamf_integration/`: IAB-BAMF-SOEP Survey of Refugees & Ukrainian Refugee Monitoring reports.
- `02_raw_data/sgb_xii_benchmarks/`: Federal Ministry of Labor and Social Affairs (BMAS) Grundsicherungsstatistik (Chapter 4, SGB XII).

---

## 2. Accessing Restricted Microdata

Official microdata from German agencies are governed by the Federal Statistics Act (*BStatG § 16*) and require Scientific Use File (SUF) data use agreements:
1. **Destatis FDZ**: Apply at [forschungsdatenzentrum.de](https://www.forschungsdatenzentrum.de) for EVS and Mikrozensus SUF.
2. **Deutsche Bundesbank RDSC**: Apply at [bundesbank.de/rdsc](https://www.bundesbank.de/en/service/research-data-and-service-centre) for PHF research files.
3. **FDZ-RV (Deutsche Rentenversicherung)**: Apply at [fdz-rv.de](https://www.fdz-rv.de) for VSKT longitudinal pension insurance accounts.
4. **IAB FDZ**: Apply at [fdz.iab.de](https://fdz.iab.de) for IAB-BAMF-SOEP survey data.

---

## 3. Automated Synthetic Pipeline

To ensure complete out-of-the-box reproducibility without requiring NDA data agreements for public users, executing `python 01_sources/build_official_datasets.py` automatically synthesizes $N = 50,000$ calibrated individual micro-records in `03_synthetic_data/` preserving all empirical marginals and covariance matrices from these official publications.
