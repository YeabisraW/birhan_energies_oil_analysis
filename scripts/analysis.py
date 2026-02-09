import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import os

# --- 1. Robust Data Loading ---
# We check multiple possible paths in case you are running from different folders
file_path = 'data/BrentOilPrices.csv'

if not os.path.exists(file_path):
    # Try looking one level up if 'data' isn't in current folder
    file_path = '../data/BrentOilPrices.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # NEW FLEXIBLE DATE CONVERSION
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
    
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)
    print(f"Successfully loaded {len(df)} rows of data.")    
    
else:
    print(f"ERROR: Could not find BrentOilPrices.csv at {os.path.abspath(file_path)}")
    print("Make sure your CSV is in the 'data' folder.")
    exit() # Stop the script here so we don't get NameError below

# --- 2. Calculations (Now safe because df exists) ---
df['Log_Returns'] = np.log(df['Price']).diff()
df['Rolling_Mean'] = df['Price'].rolling(window=252).mean()
df['Rolling_Std'] = df['Price'].rolling(window=252).std()

# --- 3. Statistical Testing ---
def perform_adf_test(series, title):
    print(f'\n--- ADF Test: {title} ---')
    result = adfuller(series.dropna())
    print(f'p-value: {result[1]:.4f}')
    if result[1] <= 0.05:
        print("Result: Stationary")
    else:
        print("Result: Non-Stationary")

perform_adf_test(df['Price'], "Raw Price")
perform_adf_test(df['Log_Returns'], "Log Returns")

# --- 4. Plotting ---
plt.figure(figsize=(12, 6))
plt.plot(df['Price'], label='Brent Price')
plt.plot(df['Rolling_Mean'], label='1-Year Trend', color='red')
plt.title('Brent Oil Price and Trend')
plt.legend()
plt.show()