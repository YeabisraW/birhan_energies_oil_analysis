import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Load and prepare data
df = pd.read_csv('data/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
df.set_index('Date', inplace=True)
# Updated .ffill() to avoid the FutureWarning
df = df.sort_index().asfreq('D').ffill()

# 2. Train/Test Split (Withhold the last 30 days)
train = df['Price'].iloc[:-30]
test = df['Price'].iloc[-30:]

# 3. Fit the ARIMA model (p=1, d=1, q=1)
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

# 4. Forecast the next 30 days
forecast_obj = model_fit.get_forecast(steps=30)
forecast = forecast_obj.predicted_mean
conf_int = forecast_obj.conf_int()

# 5. Calculate Accuracy Metrics
mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print(f"--- Forecast Accuracy ---")
print(f"MAE:  ${mae:.2f}")
print(f"RMSE: ${rmse:.2f}")

# 6. Visualization
plt.figure(figsize=(12, 6))

# Historical context
plt.plot(train.iloc[-100:].index, train.iloc[-100:].values, label="Historical (Last 100 days)", alpha=0.7)

# Actual vs Forecast (Removed 'fontweight' to fix the error)
plt.plot(test.index, test.values, label="Actual (Target)", color='black', linewidth=2)
plt.plot(test.index, forecast, label="ARIMA Forecast", color='red', linestyle='--')

# Uncertainty interval
plt.fill_between(test.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3, label="95% Confidence Interval")

plt.title(f"Brent Oil Price Prediction: ARIMA(1,1,1)\nMAE: ${mae:.2f}")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()