import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import os

def load_data(file_path):
    """Loads CSV data with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data not found at {file_path}")
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)
    return df

def compute_features(df):
    """Calculates returns and rolling stats."""
    df['Log_Returns'] = np.log(df['Price']).diff()
    df['Rolling_Mean'] = df['Price'].rolling(window=252).mean()
    return df

def run_stationarity_tests(df):
    """Performs ADF test on Price and Returns."""
    results = {}
    for col in ['Price', 'Log_Returns']:
        series = df[col].dropna()
        res = adfuller(series)
        results[col] = {'adf': res[0], 'p-value': res[1]}
    return results

if __name__ == "__main__":
    try:
        data = load_data('data/BrentOilPrices.csv')
        data = compute_features(data)
        test_results = run_stationarity_tests(data)
        print("Analysis Complete. Log Returns P-Value:", test_results['Log_Returns']['p-value'])
    except Exception as e:
        print(f"Workflow failed: {e}")