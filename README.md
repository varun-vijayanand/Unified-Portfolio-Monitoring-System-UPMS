# Unified-Portfolio-Monitoring-System-UPMS-
## Introduction
Portfolio management analytics broadly fall into two categories:
Passive Monitoring — ensuring an investment portfolio accurately replicates its benchmark (index), maintaining low tracking error and operational precision.
Active Monitoring — evaluating investment decisions, factor exposures, alpha generation, and risk management for portfolios seeking to outperform the benchmark.

This project combines both into a single, comprehensive, professional-grade system.

The Unified Portfolio Monitoring System (UPMS) automates workflows from both domains, including:

    ✔ Daily NAV & PCF reconciliation
    ✔ Index change tracking
    ✔ Corporate actions processing
    ✔ Passive Brinson attribution
    ✔ Active P&L decomposition & factor attribution.
    ✔ Alpha signal monitoring
    ✔ Risk exposure analytics
    ✔ Automated PDF/Excel report generation
    
This showcases full-spectrum buy-side analytics capability.

🧩 Key Features

🔵 Passive Portfolio Monitoring

    ✔ Daily NAV calculation & reconciliation
    ✔ PCF (Portfolio Composition File) checks
    ✔ Benchmark alignment & drift detection
    ✔ Corporate actions adjustment
    ✔ Cash balance & cash drift monitoring
    ✔ Brinson-Fachler performance attribution
    ✔ Tracking error computation
    
🔴 Active Portfolio Monitoring

    ✔ Daily P&L decomposition
    ✔ Alpha factors (momentum, value, volatility, quality, etc.)
    ✔ Factor exposure analysis (Fama-French compatible)
    ✔ Selection vs Allocation attribution
    ✔ Strategy-level drawdown monitoring
    ✔ Risk contribution by factor & security
    ✔ Intraday or daily monitoring of signals (optional upgrade)
    
🟩 Shared System Components

    ✔ Robust data loader for prices, holdings, index constituents
    ✔ Portfolio weight and return engine
    ✔ Multi-portfolio support
    ✔ End-to-end automated reporting
    ✔ Modular code design


## Project Overview
1. NAV & PCF Reconciliation (Passive Only)
   
        ✔ Ensures portfolio valuation matches expected index-compliant structure.
        ✔ Compares internal NAV vs calculated NAV
        ✔ Flags deviations
        ✔ Validates PCF weights vs fund holdings
   
2. Index vs Portfolio Monitoring (Passive Mode)
   
        ✔ Tracks index changes and portfolio drift.
        ✔ Add/delete constituents
        ✔ Weight changes
        ✔ Rebalancing drift
        ✔ Tracking error
  
3. Benchmark vs Portfolio (Active Mode)
   
      Analyzes active strategy alpha sources:
  
        ✔ Return vs benchmark
        ✔ Relative sector exposures
        ✔ Active weights
        ✔ Factor tilts
        ✔ Alpha & beta estimation
   
4. Corporate Action & Cash Flow Adjustment
      Handles:
     
        ✔ Splits
        ✔ Mergers
        ✔ Dividends
        ✔ Buybacks
        ✔ Fund inflows/outflows
   
5. Performance Attribution

    Two supported models:
    
      Passive Attribution
      
        ✔ Allocation effect
        ✔ Selection effect (drift)
        ✔ Currency effect (optional)
        
      Active Attribution
      
        ✔ Brinson-Fachler
        ✔ Factor-based (Fama-French and custom)

  
6. Risk Monitoring
   
        ✔ Sector exposure
        ✔ Volatility
        ✔ Beta
        ✔ VaR (historical simulation)
        ✔ Tracking error (passive)
        ✔ Active risk (active)


## Technologies Used
    ✔ Python
    ✔ Pandas, NumPy
    ✔ yfinance or simulated price feed
    ✔ Plotly / Matplotlib
    ✔ upyter Notebook
    ✔ Excel & HTML reporting
