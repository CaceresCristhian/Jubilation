"""
Master Pipeline Orchestrator
Executes the entire research and microsimulation pipeline from scratch in a single command.
"""

import subprocess
import sys
import time

steps = [
    ("1. Data Ingestion & Calibration", "python 01_sources/build_official_datasets.py"),
    ("2. Data Integrity Verification", "python 07_tests/test_data_integrity.py"),
    ("3. Baseline Statistical Summaries", "python 08_outputs/generate_baseline_summary.py"),
    ("4. Econometric IHS Wealth Regressions", "python 06_models_econometrics/ihs_wealth_regressions.py"),
    ("5. Mincerian Wage & Deskilling Regressions", "python 06_models_econometrics/deskilling_wage_regression.py"),
    ("6. Actuarial & Engine Unit Tests", "python 07_tests/test_simulation_engines.py"),
    ("7. Dynamic Lifecycle Microsimulation", "python 05_engine/simulation_pipeline.py"),
    ("8. Publication Figure Generation", "python 08_outputs/generate_publication_figures.py")
]

print("=" * 80)
print("STARTING COMPLETE GERMAN WEALTH & RETIREMENT PIPELINE EXECUTION")
print("=" * 80)

t0 = time.time()

for idx, (name, cmd) in enumerate(steps, 1):
    print(f"\n[{idx}/{len(steps)}] Running: {name}...")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  [ERROR] Step failed with return code {res.returncode}:")
        print(res.stderr)
        sys.exit(res.returncode)
    else:
        print(f"  [SUCCESS] {name} completed successfully.")

elapsed = time.time() - t0
print("\n" + "=" * 80)
print(f"ALL 8 PIPELINE MODULES EXECUTED IN {elapsed:.1f} SECONDS WITH ZERO ERRORS!")
print("=" * 80)
