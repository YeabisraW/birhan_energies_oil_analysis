# Task 3: Price Forecasting Results

## Model: ARIMA(1, 1, 1)
We selected an ARIMA model based on the following diagnostic findings:
* **Stationarity:** Raw prices were non-stationary (p=0.28), while first-differenced prices were stationary (p=0.00). Thus, $d=1$.
* **Lag Selection:** ACF and PACF plots suggested initial values for $p$ and $q$.

## Performance Metrics
Testing against the last 30 days of available data:
* **Mean Absolute Error (MAE):** $2.64
* **Root Mean Squared Error (RMSE):** $3.48

## Interpretation
The model captures the general trend but tends to lag during sharp market corrections. The RMSE being higher than the MAE suggests that the model is sensitive to price outliers/volatility.