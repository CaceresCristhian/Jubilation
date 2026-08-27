# IEEE Publication Manuscript & LaTeX Package

**Title:** Wealth Accumulation, Migration Dynamics, and Retirement Sustainability in Germany: A Dynamic Microdata and Econometric Policy Framework (2025–2070)  
**Format:** IEEE Conference / Journal (`IEEEtran.cls` & `ieeeaccess.cls`)  
**Main Manuscript:** [`German_Retirement_Wealth_Migration_IEEE.tex`](German_Retirement_Wealth_Migration_IEEE.tex)

---

## 1. Directory Structure

```
10_publication/
|-- IEEEtran.cls                                 # Standard IEEE Transactions / Conference LaTeX class
|-- ieeeaccess.cls                               # IEEE Access template class
|-- German_Retirement_Wealth_Migration_IEEE.tex  # Master LaTeX manuscript
|-- references.bib                               # BibTeX database with official German institutional citations
|-- figures/                                     # High-resolution charts & figures
|   |-- fig1_5way_retirement_income_and_nrr.png
|   |-- fig2_demographic_pressure_2070_oadr.png
|   |-- fig3_poverty_risk_and_savings_gap.png
|-- README.md                                    # This compilation guide
```

---

## 2. Compilation Instructions

### A. Overleaf (Recommended & Zero Setup)
1. Zip the entire `10_publication/` folder:
   - Select `IEEEtran.cls`, `German_Retirement_Wealth_Migration_IEEE.tex`, `references.bib`, and the `figures/` folder.
2. Go to [Overleaf.com](https://www.overleaf.com) $\rightarrow$ **New Project** $\rightarrow$ **Upload Project**.
3. Set the Main Document to `German_Retirement_Wealth_Migration_IEEE.tex` and click **Recompile**.

### B. Local Compilation (TeX Live / MiKTeX)
Run the standard LaTeX compilation pipeline in terminal:
```bash
pdflatex German_Retirement_Wealth_Migration_IEEE.tex
bibtex German_Retirement_Wealth_Migration_IEEE
pdflatex German_Retirement_Wealth_Migration_IEEE.tex
pdflatex German_Retirement_Wealth_Migration_IEEE.tex
```

---

## 3. Key Contents of the Manuscript

1. **Section I**: Introduction, demographic pressures (Destatis 16. BVB), and Germany's migration waves.
2. **Section II**: Institutional and statutory architecture (*SGB VI* pension formula, *SGB XII* Grundsicherung im Alter, €10,000 Schonvermögen, KVdR/PV retiree insurance).
3. **Section III**: Data architecture and $N = 50,000$ Copula synthetic microdata.
4. **Section IV**: Econometric estimations (Mincerian wage regressions with $-65.5\%$ deskilling penalty, IHS wealth regressions).
5. **Section V**: Dynamic lifecycle microsimulation outcomes for 5 cohorts up to 2070.
6. **Section VI**: Gender disaggregation and analytical boundaries.
7. **Section VII**: Policy recommendations (credential recognition, Altersvorsorgedepot, SGB XII § 82a).
8. **Section VIII**: Open science, reproducibility, and AI transparency disclosure.
