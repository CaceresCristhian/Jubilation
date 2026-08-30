"""
Publication-Grade Chart Generator
Generates publication-quality charts for reports and presentations.
"""

import os
import shutil
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set clean aesthetic styling
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["figure.dpi"] = 300

os.makedirs("08_outputs/figures", exist_ok=True)
os.makedirs("10_publication/figures", exist_ok=True)

# 1. Figure 1: 5-Way Comparison of Projected Monthly Retirement Income & NRR
df_sim = pd.read_csv("08_outputs/tables/simulated_retirement_adequacy_summary.csv")

# Clean numeric values dynamically from simulation output
pension_map = dict(zip(df_sim["Population Cohort"], df_sim["Median Projected Pension at 67 (EUR/mo)"].str.replace("€", "").str.replace(",", "").astype(float)))
total_inc_map = dict(zip(df_sim["Population Cohort"], df_sim["Median Total Ret. Income (EUR/mo)"].str.replace("€", "").str.replace(",", "").astype(float)))
nrr_map = dict(zip(df_sim["Population Cohort"], df_sim["Median Net Replacement Rate (NRR)"].str.replace("%", "").astype(float)))

cohort_keys = ["German_Native", "General_Migrant", "General_Refugee", "Ukrainian_Refugee_2022plus", "Ukrainian_Migrant_Pre2022"]
labels = ["German\nNative", "General\nMigrant", "General\nRefugee", "Ukrainian\nRefugee", "Ukrainian\nMigrant"]
pension_vals = [pension_map[k] for k in cohort_keys]
total_inc_vals = [total_inc_map[k] for k in cohort_keys]
nrr_vals = [nrr_map[k] for k in cohort_keys]

fig, ax1 = plt.subplots(figsize=(10, 5.5))

x = np.arange(len(labels))
width = 0.35

rects1 = ax1.bar(x - width/2, pension_vals, width, label="Statutory Pension (GRV)", color="#1E3A8A", alpha=0.9)
rects2 = ax1.bar(x + width/2, total_inc_vals, width, label="Total Retirement Income (incl. Private & Safety Net)", color="#0D9488", alpha=0.9)

ax1.set_ylabel("Monthly Income in Retirement (EUR 2026)", fontsize=11, fontweight="bold")
ax1.set_title("Projected Median Retirement Income at Age 67 Across Population Cohorts in Germany", fontsize=12, fontweight="bold", pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontweight="bold")
ax1.axhline(1113, color="#DC2626", linestyle="--", linewidth=1.5, label="SGB XII Poverty Threshold (€1,113/mo)")
ax1.set_ylim(0, 3200)

# Secondary axis for NRR
ax2 = ax1.twinx()
ax2.plot(x, nrr_vals, color="#D97706", marker="o", linewidth=2.5, markersize=8, label="Net Replacement Rate (NRR %)")
ax2.set_ylabel("Net Replacement Rate (%)", color="#D97706", fontsize=11, fontweight="bold")
ax2.set_ylim(0, 110)
ax2.grid(False)

# Add values on top of bars
for rect in rects1:
    h = rect.get_height()
    ax1.annotate(f"€{int(h):,}", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8)

for rect in rects2:
    h = rect.get_height()
    ax1.annotate(f"€{int(h):,}", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8, fontweight="bold")

# Legend combination
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", framealpha=0.9, fontsize=8.5)

plt.tight_layout()
fig.savefig("08_outputs/figures/fig1_5way_retirement_income_and_nrr.png", bbox_inches="tight")
shutil.copy2("08_outputs/figures/fig1_5way_retirement_income_and_nrr.png", "10_publication/figures/fig1_5way_retirement_income_and_nrr.png")
plt.close(fig)
print("  -> Generated fig1_5way_retirement_income_and_nrr.png")


# 2. Figure 2: Demographic Pressure 2024-2070 (Destatis 16. BVB)
df_demog = pd.read_csv("04_processed/destatis_demographics_16_bvb_2024_2070.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

years = df_demog[df_demog["variant"] == "V1_Moderate_G2_L2_W2"]["year"].values
pop_67_v1 = df_demog[df_demog["variant"] == "V1_Moderate_G2_L2_W2"]["pop_age_67plus_retirement_age_millions"].values
pop_67_v2 = df_demog[df_demog["variant"] == "V2_AgingShock_G1_L3_W1"]["pop_age_67plus_retirement_age_millions"].values
pop_67_v3 = df_demog[df_demog["variant"] == "V3_HighMigration_G3_L2_W3"]["pop_age_67plus_retirement_age_millions"].values

ax1.plot(years, pop_67_v1, label="V1: Moderate Migration (+250k/yr)", color="#1E3A8A", linewidth=2.5)
ax1.plot(years, pop_67_v2, label="V2: Aging Shock (Low Mig.)", color="#DC2626", linestyle="--", linewidth=2)
ax1.plot(years, pop_67_v3, label="V3: High Migration (+400k/yr)", color="#059669", linestyle="-.", linewidth=2)
ax1.set_title("Retirement Age Population (67+ Years)", fontweight="bold")
ax1.set_xlabel("Year")
ax1.set_ylabel("Population (Millions)")
ax1.legend(loc="lower right", fontsize=8.5)

oadr_v1 = df_demog[df_demog["variant"] == "V1_Moderate_G2_L2_W2"]["old_age_dependency_ratio_oadr_pct"].values
oadr_v2 = df_demog[df_demog["variant"] == "V2_AgingShock_G1_L3_W1"]["old_age_dependency_ratio_oadr_pct"].values
oadr_v3 = df_demog[df_demog["variant"] == "V3_HighMigration_G3_L2_W3"]["old_age_dependency_ratio_oadr_pct"].values

ax2.plot(years, oadr_v1, label="V1: Moderate", color="#1E3A8A", linewidth=2.5)
ax2.plot(years, oadr_v2, label="V2: Aging Shock", color="#DC2626", linestyle="--", linewidth=2)
ax2.plot(years, oadr_v3, label="V3: High Migration", color="#059669", linestyle="-.", linewidth=2)
ax2.set_title("Old-Age Dependency Ratio (OADR: Pop 67+ / Pop 20-66)", fontweight="bold")
ax2.set_xlabel("Year")
ax2.set_ylabel("OADR (%)")
ax2.set_ylim(30, 60)
ax2.axhline(50.0, color="gray", linestyle=":", label="50% Threshold (2 Workers : 1 Retiree)")
ax2.legend(loc="upper left", fontsize=8.5)

plt.suptitle("Destatis 16. BVB Demographic Projections & System Dependency Pressure (Germany 2024-2070)", fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
fig.savefig("08_outputs/figures/fig2_demographic_pressure_2070_oadr.png", bbox_inches="tight")
shutil.copy2("08_outputs/figures/fig2_demographic_pressure_2070_oadr.png", "10_publication/figures/fig2_demographic_pressure_2070_oadr.png")
plt.close(fig)
print("  -> Generated fig2_demographic_pressure_2070_oadr.png")


# 3. Figure 3: Poverty Risk & Required Additional Savings S*
fig, ax = plt.subplots(figsize=(9, 5))

# Compute poverty rates (% below 1113 EUR) directly from simulation summary
poverty_avoidance_map = dict(zip(df_sim["Population Cohort"], df_sim["Poverty Avoidance Rate (%)"].str.replace("%", "").astype(float)))
poverty_rates = [100.0 - poverty_avoidance_map[k] for k in cohort_keys]

x = np.arange(len(labels))
bars = ax.bar(x, poverty_rates, color=["#10B981", "#F59E0B", "#F59E0B", "#EF4444", "#F59E0B"], width=0.5, edgecolor="black", linewidth=0.5)

ax.set_ylabel("Retirement Poverty Shortfall Risk (%)", fontsize=11, fontweight="bold")
ax.set_title("Share of Cohort with Autonomous Retirement Income Below Subsistence Minimum (<€1,113/mo)", fontsize=11, fontweight="bold", pad=12)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontweight="bold")
ax.set_ylim(0, 65)

for bar, rate in zip(bars, poverty_rates):
    y = bar.get_height()
    ax.annotate(f"{rate:.1f}%", xy=(bar.get_x() + bar.get_width()/2, y), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontweight="bold", fontsize=9)

plt.tight_layout()
fig.savefig("08_outputs/figures/fig3_poverty_risk_and_savings_gap.png")
shutil.copy2("08_outputs/figures/fig3_poverty_risk_and_savings_gap.png", "10_publication/figures/fig3_poverty_risk_and_savings_gap.png")
plt.close(fig)
print("  -> Generated fig3_poverty_risk_and_savings_gap.png")

print("\nAll publication-grade charts generated successfully in 08_outputs/figures/ and 10_publication/figures/!")
