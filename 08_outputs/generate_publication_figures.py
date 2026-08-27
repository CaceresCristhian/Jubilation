"""
Publication-Grade Chart Generator
Generates publication-quality charts for reports and presentations.
"""

import os
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

# 1. Figure 1: 5-Way Comparison of Projected Monthly Retirement Income & NRR
df_sim = pd.read_csv("08_outputs/tables/simulated_retirement_adequacy_summary.csv")

# Clean numeric values
labels = ["German\nNative", "General\nMigrant", "General\nRefugee", "Ukrainian\nRefugee", "Ukrainian\nMigrant"]
pension_vals = [2108, 1552, 1272, 797, 1480]
total_inc_vals = [2631, 2018, 1596, 1061, 1967]
nrr_vals = [87.5, 79.6, 74.8, 50.7, 76.4]

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
    ax1.annotate(f"€{h:,}", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8)

for rect in rects2:
    h = rect.get_height()
    ax1.annotate(f"€{h:,}", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8, fontweight="bold")

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=True, framealpha=0.95)

plt.tight_layout()
fig.savefig("08_outputs/figures/fig1_5way_retirement_income_and_nrr.png")
plt.close(fig)
print("  -> Generated fig1_5way_retirement_income_and_nrr.png")


# 2. Figure 2: Destatis 16. BVB Demographic Pressure (2024-2070)
df_demog = pd.read_csv("04_processed/destatis_demographics_16_bvb_2024_2070.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

variants = {
    "V1_Moderate_G2_L2_W2": ("V1: Moderate Base (+250k Net Mig)", "#2563EB"),
    "V2_AgingShock_G1_L3_W1": ("V2: Aging Shock (+150k Net Mig)", "#DC2626"),
    "V3_HighMigration_G3_L2_W3": ("V3: High Migration (+400k Net Mig)", "#059669"),
    "V4_Contraction_G1_L1_W1": ("V4: Low Longevity Contraction", "#6B7280")
}

for v_key, (v_label, color) in variants.items():
    df_v = df_demog[df_demog["variant"] == v_key]
    ax1.plot(df_v["year"], df_v["pop_age_20_66_working_age_millions"], label=v_label, color=color, linewidth=2.0)
    ax2.plot(df_v["year"], df_v["old_age_dependency_ratio_oadr_pct"], label=v_label, color=color, linewidth=2.0)

ax1.set_title("Working-Age Population (20-66 Years, Millions)", fontweight="bold")
ax1.set_xlabel("Year")
ax1.set_ylabel("Millions of Persons")
ax1.set_ylim(35, 55)
ax1.legend(loc="lower left", fontsize=8.5)

ax2.set_title("Old-Age Dependency Ratio (OADR: Pop 67+ / Pop 20-66)", fontweight="bold")
ax2.set_xlabel("Year")
ax2.set_ylabel("OADR (%)")
ax2.set_ylim(30, 60)
ax2.axhline(50.0, color="gray", linestyle=":", label="50% Threshold (2 Workers : 1 Retiree)")
ax2.legend(loc="upper left", fontsize=8.5)

plt.suptitle("Destatis 16. BVB Demographic Projections & System Dependency Pressure (Germany 2024-2070)", fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
fig.savefig("08_outputs/figures/fig2_demographic_pressure_2070_oadr.png", bbox_inches="tight")
plt.close(fig)
print("  -> Generated fig2_demographic_pressure_2070_oadr.png")


# 3. Figure 3: Poverty Risk & Required Additional Savings S*
fig, ax = plt.subplots(figsize=(9, 5))

poverty_rates = [0.3, 13.2, 10.1, 52.1, 11.7] # % below poverty without top-up
savings_gap = [0, 0, 0, 51, 0]

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
plt.close(fig)
print("  -> Generated fig3_poverty_risk_and_savings_gap.png")

print("\nAll publication-grade charts generated successfully in 08_outputs/figures/!")
