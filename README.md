# Brent Oil Price Analysis: Geopolitical & Economic Impact
# Analysis for Birhan Energies
This project analyzes the historical volatility of Brent Crude oil prices (1987–2022). We utilize Bayesian Inference to detect structural breaks and Time-Series Econometrics (ARIMA/GARCH) to forecast prices and quantify market risk.

📊 Project Milestones & Results
# Task 1: Data Preparation & EDA
Stationarity: Confirmed raw prices are non-stationary (p \approx 0.28). First-differenced prices are stationary (p < 0.001), establishing the foundation for forecasting.
Event Correlation: Mapped 15+ geopolitical events (OPEC shifts, 2008 crisis, etc.) against price fluctuations.

# Task 2: Bayesian Change Point Analysis
Methodology: Implemented a Bayesian MCMC model to detect structural shifts.Finding: Successfully identified the 2014 Price Collapse as a definitive regime shift rather than a temporary dip, with the mean price dropping from approx $103.60 to approx $53.99.

# Task 3: Forecasting & Risk Modeling
ARIMA(1,1,1): Achieved a Mean Absolute Error (MAE) of $2.64, providing Birhan Energies with a reliable 30-day budgeting baseline.
GARCH(1,1): Detected a Volatility Persistence (beta) of 0.9051.
Strategic Insight: Because beta > 0.90, market "shocks" take a significant amount of time to decay. The company should expect high-risk conditions to persist for weeks following any major geopolitical event.

# Project Structure
data/: Geopolitical events ledger (oil_events.csv) and raw price data.
scripts/:
bayesian_modeling.py: MCMC sampling for regime shifts.
arima_forecast.py: Predictive price modeling.
volatility_analysis.py: GARCH risk assessment.
docs/: Comprehensive workflow, results documentation, and visualization exports.

# Setup & Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/YeabisraW/birhan_energies_oil_analysis.git

2. Install dependencies:
```bash
pip install pandas numpy matplotlib pymc arviz statsmodels arch

3. Run the primary forecast:
```bash
python scripts/arima_forecast.py


📈 Stakeholder ImpactBy combining regime-shift detection with volatility persistence modeling, this analysis allows Birhan Energies to:Optimize Procurement: Use the ARIMA forecast to timing fuel purchases within a $\pm \$2.64$ confidence window.Manage Risk: Use GARCH insights to adjust hedge positions during high-volatility "clusters."
