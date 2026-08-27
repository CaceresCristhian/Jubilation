"""
Econometric Estimation: Inverse Hyperbolic Sine (IHS) Wealth Regressions
Tests Hypotheses H1 (Initial Wealth Gap) and H2 (Assimilation by Duration of Residence).

Implemented using pure NumPy & SciPy for zero-dependency execution with robust (HC1/HC3) standard errors.
"""

import pandas as pd
import numpy as np
from scipy import stats

def ihs_transform(y: np.ndarray, theta: float = 1.0) -> np.ndarray:
    """Inverse Hyperbolic Sine transformation: ln(theta*y + sqrt((theta*y)^2 + 1)) / theta"""
    return np.log(theta * y + np.sqrt((theta * y) ** 2 + 1.0)) / theta

def fit_ols_robust(y: np.ndarray, X: np.ndarray, var_names: list) -> dict:
    """Fits OLS regression with HC1 robust standard errors."""
    N, K = X.shape
    # OLS coefficients: (X'X)^(-1) X' y
    beta = np.linalg.solve(X.T @ X, X.T @ y)
    residuals = y - X @ beta
    
    # HC1 Robust Covariance: (N / (N - K)) * (X'X)^(-1) (X' diag(e^2) X) (X'X)^(-1)
    inv_XX = np.linalg.inv(X.T @ X)
    meat = X.T @ (residuals[:, None] ** 2 * X)
    cov_hc1 = (N / (N - K)) * (inv_XX @ meat @ inv_XX)
    
    se = np.sqrt(np.diag(cov_hc1))
    t_stat = beta / se
    p_val = stats.t.sf(np.abs(t_stat), df=N - K) * 2.0
    
    # R-squared
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    ss_res = np.sum(residuals ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    
    return {
        "params": dict(zip(var_names, beta)),
        "bse": dict(zip(var_names, se)),
        "tvalues": dict(zip(var_names, t_stat)),
        "pvalues": dict(zip(var_names, p_val)),
        "rsquared": r2,
        "nobs": N
    }

print("=" * 80)
print("RUNNING ECONOMETRIC ESTIMATION: IHS WEALTH REGRESSIONS (H1 & H2)")
print("=" * 80)

# Load microdata
df = pd.read_parquet("03_synthetic_data/synthetic_individual_microdata.parquet")
df_working = df[(df["age"] >= 25) & (df["age"] <= 64)].copy()

# Dependent variables
df_working["ihs_financial_wealth"] = ihs_transform(df_working["financial_wealth_eur"].values)
df_working["ihs_net_wealth"] = ihs_transform(df_working["net_wealth_eur"].values)

# Construct explanatory variables
df_working["const"] = 1.0
df_working["age_sq"] = (df_working["age"] ** 2) / 100.0 # scaled for numerical precision
df_working["years_in_de_sq"] = (df_working["years_in_germany"] ** 2) / 100.0
df_working["is_female"] = (df_working["sex"] == "Female").astype(float)
df_working["edu_tertiary"] = (df_working["education_level"] == "High (Tertiary)").astype(float)
df_working["edu_vocational"] = (df_working["education_level"] == "Medium (Vocational)").astype(float)

# Group dummies (Reference: German_Native)
groups = ["General_Migrant", "General_Refugee", "Ukrainian_Refugee_2022plus", "Ukrainian_Migrant_Pre2022"]
for g in groups:
    df_working[f"group_{g}"] = (df_working["population_group"] == g).astype(float)

covariates = [
    "const",
    "group_General_Migrant",
    "group_General_Refugee",
    "group_Ukrainian_Refugee_2022plus",
    "group_Ukrainian_Migrant_Pre2022",
    "age",
    "age_sq",
    "years_in_germany",
    "years_in_de_sq",
    "is_female",
    "edu_tertiary",
    "edu_vocational"
]

X_mat = df_working[covariates].values

# 1. Financial Wealth Regression
res_fin = fit_ols_robust(df_working["ihs_financial_wealth"].values, X_mat, covariates)

# 2. Net Wealth Regression
res_net = fit_ols_robust(df_working["ihs_net_wealth"].values, X_mat, covariates)

# Summarize results
reg_table = []
for var in covariates:
    reg_table.append({
        "Variable": var,
        "Fin_Wealth_Coef": round(res_fin["params"][var], 3),
        "Fin_Wealth_SE": round(res_fin["bse"][var], 3),
        "Fin_Wealth_pValue": f"{res_fin['pvalues'][var]:.4f}" if res_fin['pvalues'][var] >= 0.0001 else "<0.0001",
        "Net_Wealth_Coef": round(res_net["params"][var], 3),
        "Net_Wealth_SE": round(res_net["bse"][var], 3),
        "Net_Wealth_pValue": f"{res_net['pvalues'][var]:.4f}" if res_net['pvalues'][var] >= 0.0001 else "<0.0001"
    })

df_reg = pd.DataFrame(reg_table)
df_reg.to_csv("08_outputs/tables/econometric_ihs_wealth_regressions.csv", index=False)

# Custom Markdown
headers = list(df_reg.columns)
lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + "|"]
for _, r in df_reg.iterrows():
    lines.append("| " + " | ".join(str(r[h]) for h in headers) + " |")
md_table = "\n".join(lines)

with open("08_outputs/reports/econometric_ihs_wealth_report.md", "w", encoding="utf-8") as f:
    f.write("# Econometric Results: IHS Wealth Regressions (H1 & H2 Tests)\n\n")
    f.write("**Model:** OLS with Robust Standard Errors (HC1) on Inverse Hyperbolic Sine of Wealth\n\n")
    f.write(md_table + "\n\n")
    f.write(f"- Financial Wealth $R^2$: {res_fin['rsquared']:.4f} (N = {res_fin['nobs']:,})\n")
    f.write(f"- Net Wealth $R^2$: {res_net['rsquared']:.4f} (N = {res_net['nobs']:,})\n")

print("Estimation completed successfully. Saved to 08_outputs/tables/ & 08_outputs/reports/.\n")
print(md_table)
