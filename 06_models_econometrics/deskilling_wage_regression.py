"""
Econometric Estimation: Mincerian Wage Equations with Deskilling Penalties & Language Premiums
Tests Hypotheses H3 (Deskilling & Refugee Penalty) and H4 (Language & Human Capital).

Model:
ln(GrossWage_i) = beta_0 + beta_1 * Experience_DE_i + beta_2 * Experience_DE_i^2
                  + beta_3 * Tertiary_Edu_i + beta_4 * Vocational_Edu_i
                  + beta_5 * German_B2_C2_i - beta_6 * DeskillingPenalty_i
                  + beta_7 * Female_i + beta_8 * CohortDummies_i + epsilon_i
"""

import pandas as pd
import numpy as np
from scipy import stats

def fit_ols_robust(y: np.ndarray, X: np.ndarray, var_names: list) -> dict:
    N, K = X.shape
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    residuals = y - X @ beta
    inv_XX = np.linalg.inv(X.T @ X)
    meat = X.T @ (residuals[:, None] ** 2 * X)
    cov_hc1 = (N / (N - K)) * (inv_XX @ meat @ inv_XX)
    se = np.sqrt(np.diag(cov_hc1))
    t_stat = beta / se
    p_val = stats.t.sf(np.abs(t_stat), df=N - K) * 2.0
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    ss_res = np.sum(residuals ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    return {
        "params": dict(zip(var_names, beta)),
        "bse": dict(zip(var_names, se)),
        "pvalues": dict(zip(var_names, p_val)),
        "rsquared": r2,
        "nobs": N
    }

print("=" * 80)
print("RUNNING ECONOMETRIC ESTIMATION: WAGE EQUATIONS & DESKILLING (H3 & H4)")
print("=" * 80)

df = pd.read_parquet("03_synthetic_data/synthetic_individual_microdata.parquet")
df_employed = df[(df["age"] >= 25) & (df["age"] <= 64) & (df["annual_gross_wage_eur"] > 0)].copy()

df_employed["log_wage"] = np.log(df_employed["annual_gross_wage_eur"].values)
df_employed["const"] = 1.0
df_employed["exp_de"] = np.minimum(df_employed["age"] - 18.0, df_employed["years_in_germany"])
df_employed["exp_de_sq"] = (df_employed["exp_de"] ** 2) / 100.0
df_employed["is_female"] = (df_employed["sex"] == "Female").astype(float)
df_employed["edu_tertiary"] = (df_employed["education_level"] == "High (Tertiary)").astype(float)
df_employed["edu_vocational"] = (df_employed["education_level"] == "Medium (Vocational)").astype(float)
df_employed["lang_advanced_b2_c2"] = df_employed["german_language_cefr"].isin(["B2", "C1/C2"]).astype(float)

groups = ["General_Migrant", "General_Refugee", "Ukrainian_Refugee_2022plus", "Ukrainian_Migrant_Pre2022"]
for g in groups:
    df_employed[f"group_{g}"] = (df_employed["population_group"] == g).astype(float)

covariates = [
    "const",
    "group_General_Migrant",
    "group_General_Refugee",
    "group_Ukrainian_Refugee_2022plus",
    "group_Ukrainian_Migrant_Pre2022",
    "exp_de",
    "exp_de_sq",
    "edu_tertiary",
    "edu_vocational",
    "lang_advanced_b2_c2",
    "deskilling_penalty",
    "is_female"
]

X_mat = df_employed[covariates].values
res_wage = fit_ols_robust(df_employed["log_wage"].values, X_mat, covariates)

reg_table = []
for var in covariates:
    reg_table.append({
        "Variable": var,
        "Coefficient": round(res_wage["params"][var], 4),
        "Robust_SE": round(res_wage["bse"][var], 4),
        "pValue": f"{res_wage['pvalues'][var]:.4f}" if res_wage['pvalues'][var] >= 0.0001 else "<0.0001",
        "Pct_Wage_Effect": f"{(np.exp(res_wage['params'][var]) - 1.0) * 100:+.2f}%" if var != "const" else "-"
    })

df_reg = pd.DataFrame(reg_table)
df_reg.to_csv("08_outputs/tables/econometric_wage_deskilling_regressions.csv", index=False)

headers = list(df_reg.columns)
lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + "|"]
for _, r in df_reg.iterrows():
    lines.append("| " + " | ".join(str(r[h]) for h in headers) + " |")
md_table = "\n".join(lines)

with open("08_outputs/reports/econometric_wage_deskilling_report.md", "w", encoding="utf-8") as f:
    f.write("# Econometric Results: Wage Dynamics, Qualification Deskilling & Language Premiums\n\n")
    f.write(md_table + "\n\n")
    f.write("- Dependent Variable: ln(Annual Gross Wage)\n")
    f.write(f"- Sample Size (N): {res_wage['nobs']:,} employed individuals\n")
    f.write(f"- Model R-squared: {res_wage['rsquared']:.4f}\n")

print("Wage regression completed successfully:\n")
print(md_table)
