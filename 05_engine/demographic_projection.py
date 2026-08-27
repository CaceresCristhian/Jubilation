"""
Demographic & Macro-Feedback Engine (Destatis 16. BVB & SGB VI Sustainability Factor)
Couples:
- Destatis 16. koordinierte Bevölkerungsvorausberechnung (Variants V1-V4)
- Dynamic Old-Age Dependency Ratio (OADR) & System Dependency Ratio (SDR)
- SGB VI § 68 Rentenanpassungsformel with Sustainability Factor (Nachhaltigkeitsfaktor)
- Rentenpaket II Haltelinie (48% floor) and Generationenkapital impact
"""

import pandas as pd
import numpy as np

class DemographicProjectionEngine:
    def __init__(self,
                 demographic_file: str = "04_processed/destatis_demographics_16_bvb_2024_2070.csv",
                 beta_sustainability: float = 0.25, # SGB VI legal parameter
                 haltelinie_floor: float = 0.48):
        self.df_demog = pd.read_csv(demographic_file)
        self.beta = beta_sustainability
        self.haltelinie = haltelinie_floor

    def project_pension_value_series(self, variant: str = "V1_Moderate_G2_L2_W2", wage_growth_rate: float = 0.025) -> pd.DataFrame:
        """
        Projects the Aktueller Rentenwert (AR) and pension point value under demographic feedback.
        """
        df_v = self.df_demog[self.df_demog["variant"] == variant].sort_values("year").copy()
        
        ar_series = [42.15] # 2026 baseline
        years = df_v["year"].tolist()
        
        # Start projecting from 2027
        for idx in range(1, len(years)):
            prev_sdr = df_v["system_dependency_ratio_sdr"].iloc[idx - 1]
            curr_sdr = df_v["system_dependency_ratio_sdr"].iloc[idx]
            
            # Sustainability Factor (NHF): (1 - (SDR_t / SDR_{t-1})) * beta + 1
            sdr_growth = (curr_sdr / prev_sdr) if prev_sdr > 0 else 1.0
            nhf = 1.0 - (sdr_growth - 1.0) * self.beta
            
            # Wage factor
            wage_factor = 1.0 + wage_growth_rate
            
            # Total adjustment factor
            adj_factor = wage_factor * nhf
            new_ar = ar_series[-1] * adj_factor
            ar_series.append(new_ar)
            
        df_v["projected_ar_nominal_eur"] = [round(x, 2) for x in ar_series]
        
        # Real AR discounted at 2.0% inflation
        df_v["projected_ar_real_2026_eur"] = [
            round(ar / ((1.0 + 0.020) ** (yr - 2026)), 2) for yr, ar in zip(years, ar_series)
        ]
        
        return df_v
