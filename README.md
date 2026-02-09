# Brent Oil Price Analysis: Geopolitical & Economic Impact

## Overview
This project, conducted for **Birhan Energies**, analyzes the historical volatility of Brent Crude oil prices (1987–2022). We use **Bayesian Change Point Analysis** to detect structural breaks in the market and correlate them with major geopolitical events, OPEC policy shifts, and global economic crises.

## Project Structure
- `data/`: Contains researched geopolitical events (`oil_events.csv`). *Note: Raw price data is kept locally due to size.*
- `notebooks/`: Exploratory Data Analysis (EDA) and Bayesian Modeling.
- `scripts/`: Python scripts for data processing and stationarity testing.
- `docs/`: Project workflow, assumptions, and limitations.

## Task 1: Key Findings (Interim)
- **Stationarity:** Raw Brent prices are non-stationary ($p \approx 0.28$). However, **Log Returns** are stationary ($p < 0.01$), making them the ideal candidate for modeling price shocks.
- **Event Ledger:** We have identified 15 key historical events, including the 2008 Financial Crisis, the 2014 OPEC Price War, and the 2022 Ukraine Invasion, to serve as "ground truth" for our model.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/YeabisraW/birhan_energies_oil_analysis.git](https://github.com/YeabisraW/birhan_energies_oil_analysis.git)
2. Install dependencies:
   ```bash     
   pip install pandas numpy matplotlib pymc arviz statsmodels
3. Run the analysis:
   ```bash
   python scripts/analysis.py
# Future Work (Task 2 & 3)
## Execute Bayesian MCMC sampling using PyMC to quantify the impact of specific events.
## Develop an interactive React/Flask dashboard to visualize these structural breaks for stakeholders.   
