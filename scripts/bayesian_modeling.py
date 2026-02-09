import pymc as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az
import os

def run_bayesian_change_point(data_path, start_date, end_date):
    """
    Identifies a structural break in oil prices using Bayesian Inference.
    """
    # 1. Load and Prepare Data
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
    df.set_index('Date', inplace=True)
    
    # Filter for the specific event window (e.g., 2014 crash)
    subset = df.loc[start_date:end_date]['Price']
    prices = subset.values
    idx = np.arange(len(prices))
    
    print(f"Sampling model for period: {start_date} to {end_date}...")

    # 2. Define the Bayesian Model
    with pm.Model() as model:
        # Prior for the switch point (Tau) - the date the regime changed
        tau = pm.DiscreteUniform("tau", lower=0, upper=len(prices) - 1)
        
        # Priors for the mean prices (Regime Parameters)
        mu_1 = pm.Normal("mu_1", mu=prices.mean(), sigma=20)
        mu_2 = pm.Normal("mu_2", mu=prices.mean(), sigma=20)
        
        # Prior for market volatility (Sigma)
        sigma = pm.HalfNormal("sigma", sigma=10)
        
        # The Logic: Switch the mean from mu_1 to mu_2 at time tau
        mu_regime = pm.math.switch(tau > idx, mu_1, mu_2)
        
        # Likelihood: The relationship between our model and real data
        obs = pm.Normal("obs", mu=mu_regime, sigma=sigma, observed=prices)
        
        # 3. Inference: MCMC Sampling
        trace = pm.sample(2000, tune=1000, return_inferencedata=True, target_accept=0.9)
        
    return subset, trace

def plot_and_save_results(subset, trace, event_name):
    """Generates the visualization and summary statistics."""
    summary = az.summary(trace, var_names=["mu_1", "mu_2", "tau"])
    tau_mean = int(summary.loc['tau', 'mean'])
    detected_date = subset.index[tau_mean]
    
    plt.figure(figsize=(12, 6))
    plt.plot(subset.index, subset.values, label="Actual Brent Price", alpha=0.6)
    
    # Overlay the detected regimes
    plt.hlines(summary.loc['mu_1', 'mean'], subset.index[0], detected_date, 
               colors='red', linestyles='--', label="Regime 1 (Pre-Crash)")
    plt.hlines(summary.loc['mu_2', 'mean'], detected_date, subset.index[-1], 
               colors='green', linestyles='--', label="Regime 2 (Post-Crash)")
    
    plt.axvline(detected_date, color='black', linestyle=':', label=f"Break Point: {detected_date.date()}")
    plt.title(f"Bayesian Analysis: {event_name}")
    plt.ylabel("Price (USD)")
    plt.legend()
    
    # Save the plot for the report
    plt.savefig(f"docs/change_point_{event_name.replace(' ', '_')}.png")
    print(f"Plot saved to docs/change_point_{event_name.replace(' ', '_')}.png")
    plt.show()

if __name__ == "__main__":
    # Point this to your data folder
    data_file = 'data/BrentOilPrices.csv'
    
    # Analyze the 2014-2015 "Price War" period
    data_subset, model_trace = run_bayesian_change_point(data_file, '2014-01-01', '2015-12-31')
    
    # Output the statistical summary for the report
    print("\n--- Model Results ---")
    print(az.summary(model_trace, var_names=["mu_1", "mu_2", "tau"]))
    
    plot_and_save_results(data_subset, model_trace, "2014 Price Collapse")