Project Workflow & Analysis Framework
1. Project Overview
This project analyzes the impact of significant geopolitical and economic events on Brent Crude oil prices. The objective is to move beyond simple price tracking and into quantifying structural shifts in the market using Bayesian inference.

2. Research & Data Strategy
Data Sources
Brent Oil Prices: Daily historical data (1987–2022).

Event Ledger: A curated list of 15+ global events (OPEC decisions, conflicts, financial crises) sourced from historical market reports and energy archives.

Assumptions & Limitations
Efficiency: We assume market participants react to geopolitical news in a way that manifests as structural breaks in price or volatility.

Lagged Effects: We acknowledge that policy changes (like interest rate shifts) may have delayed impacts on physical supply, though price speculation is often immediate.

Confounding Variables: Oil prices are influenced by a complex mix of factors. A drop during a war may be due to a simultaneous global demand slump.

3. Analysis Methodology

Time Series PropertiesBased on our Exploratory Data Analysis (EDA), I have identified:Non-Stationarity: Raw prices show significant trends and drift.Stationary Transformation: Log Returns are highly stationary and will be the primary input for modeling.Volatility Clustering: Shocks tend to appear in groups, corresponding to periods of geopolitical instability.Correlation vs. CausationWe distinguish between correlation (events happening at the same time as price shifts) and causation (direct proof that Event A moved the price). Our Bayesian approach provides probabilistic evidence of impact, reducing but not eliminating the "causality gap."

4. Bayesian Change Point Modeling

To identify structural breaks, we utilize PyMC for Markov Chain Monte Carlo (MCMC) sampling.Why this model? Unlike moving averages, Change Point models detect the exact "switch" in market regimes.
Expected Outputs:Tau: The most probable date the regime shift occurred.
mu_1 & mu_2: The average log-returns (or price) before and after the shift.Uncertainty Interval: The confidence range for the detected change date.

5. Communication & Stakeholder Insights

To ensure the analysis is actionable, insights will be communicated as follows:

Stakeholder,Communication Channel,Key Focus
Investors,Quarterly Reports / Dashboards,Risk exposure and volatility regimes.
Policymakers,Policy Briefings,Impact of sanctions and production quotas on stability.
Energy Companies,Strategic Briefings,Long-term price floor/ceiling shifts for contract planning.