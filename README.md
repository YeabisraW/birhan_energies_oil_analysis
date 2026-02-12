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

# Dashboard Architecture
The project includes a full-stack interactive dashboard:
Backend: Flask API serving Brent Oil data and geopolitical event markers.
Frontend: React with Recharts for high-fidelity, interactive time-series visualization.
Features: Live status connectivity, KPI metrics (MAE/RMSE), and hover-interactive event tooltips.
# Project Structure
birhan_energies_oil_analysis/
├── data/                  # Raw BrentOilPrices.csv and event ledger
├── scripts/               # Statistical modeling scripts (PyMC, GARCH)
├── dashboard/             
│   ├── backend/           # Flask app.py and API logic
│   └── frontend/          # React App.js and UI components
└── docs/                  # Visualization exports and Interim Reports
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


4. Launch Backend (Flask)
```bash
cd dashboard/backend
pip install flask flask-cors pandas
python app.py

5. Launch Frontend (React)
```bash
cd dashboard/frontend
npm install axios recharts
npm start


## 🔍 Bayesian Regime Shift Analysis
The Bayesian Discrete Uniform model successfully identified a structural break in the Brent Oil market.

* **Break Date Detected:** 2014-11-13 (Correlates with the 2014 Global Supply Glut/OPEC Policy Shift).
* **Regime 1 Mean (Pre-Crash):** $103.57
* **Regime 2 Mean (Post-Crash):** $53.97
* **Quantitative Impact:** A **-47.89%** structural shift in price baseline.
* **Convergence Diagnostics:** Achieved an **R-hat of 1.0**, confirming that the MCMC sampling has fully converged and the results are statistically robust.

📈 Stakeholder Impact
By combining regime-shift detection with volatility persistence modeling, Birhan Energies can:
Optimize Procurement: Time fuel purchases within a pm $2.64 confidence window based on ARIMA forecasts.
Manage Risk: Use GARCH insights to identify "Volatility Clusters," adjusting hedge positions when persistence (beta) exceeds 0.9.
Operational Planning: Differentiate between "Noise" and "Regime Shifts" using Bayesian change-point logic.