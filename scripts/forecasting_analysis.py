import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# 1. Load data
df = pd.read_csv('data/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
df.set_index('Date', inplace=True)

def test_stationarity(series, name):
    print(f"\n--- Testing Stationarity for: {name} ---")
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    if result[1] <= 0.05:
        print("Conclusion: Data is Stationary (Safe to forecast)")
    else:
        print("Conclusion: Data is NOT Stationary (Needs differencing)")

# Check raw prices
test_stationarity(df['Price'], "Raw Oil Prices")

# Check first difference (Price today minus Price yesterday)
test_stationarity(df['Price'].diff().dropna(), "First Differenced Prices")
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Create a figure for ACF and PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Plot ACF (helps find 'q')
plot_acf(df['Price'].diff().dropna(), lags=40, ax=ax1)
ax1.set_title("Autocorrelation (ACF) - Helps find 'q'")

# Plot PACF (helps find 'p')
plot_pacf(df['Price'].diff().dropna(), lags=40, ax=ax2)
ax2.set_title("Partial Autocorrelation (PACF) - Helps find 'p'")

plt.tight_layout()
plt.show()
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Create a figure for ACF and PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Plot ACF (helps find 'q')
plot_acf(df['Price'].diff().dropna(), lags=40, ax=ax1)
ax1.set_title("Autocorrelation (ACF) - Helps find 'q'")

# Plot PACF (helps find 'p')
plot_pacf(df['Price'].diff().dropna(), lags=40, ax=ax2)
ax2.set_title("Partial Autocorrelation (PACF) - Helps find 'p'")

plt.tight_layout()
plt.show()
