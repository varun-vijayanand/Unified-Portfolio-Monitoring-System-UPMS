import os

folders = [
    "data",
    "data/sample_output",
    "notebooks",
    "src/common",
    "src/passive_monitoring",
    "src/active_monitoring"
]

files = [
    "data/portfolio_active.csv",
    "data/portfolio_passive.csv",
    "data/index_constituents.csv",
    "data/prices.csv",
    "data/corporate_actions.csv",
    "data/cash_flows.csv",
    "data/factor_data.csv",
    "notebooks/unified_monitoring_notebook.ipynb",
    "src/common/data_loader.py",
    "src/common/pricing_engine.py",
    "src/common/portfolio_utils.py",
    "src/common/reporting.py",
    "src/passive_monitoring/nav_reconciliation.py",
    "src/passive_monitoring/pcf_reconciliation.py",
    "src/passive_monitoring/index_alignment.py",
    "src/passive_monitoring/corporate_actions_processor.py",
    "src/passive_monitoring/passive_attribution.py",
    "src/active_monitoring/alpha_factors.py",
    "src/active_monitoring/active_attribution.py",
    "src/active_monitoring/pnl_decomposition.py",
    "src/active_monitoring/factor_exposure.py",
    "src/active_monitoring/strategy_risk_monitor.py",
    "README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created successfully!")
