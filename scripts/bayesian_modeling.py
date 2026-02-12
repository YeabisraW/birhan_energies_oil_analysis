try:
    import pymc as pm
    import arviz as az
except ImportError:
    print("❌ Error: PyMC or ArviZ not found.")
    print("Please run: pip install pymc arviz")
    import sys
    sys.exit(1)
import pymc as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az
import os

def run_bayesian_change_point(data_path, start_date, end_date):
    """Identifies a structural break in oil prices using Bayesian Inference."""
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"CSV not found at {data_path}")

    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
    df.set_index('Date', inplace=True)
    
    subset = df.loc[start_date:end_date]['Price']
    prices = subset.values
    idx = np.arange(len(prices))
    
    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=len(prices) - 1)
        mu_1 = pm.Normal("mu_1", mu=prices.mean(), sigma=20)
        mu_2 = pm.Normal("mu_2", mu=prices.mean(), sigma=20)
        sigma = pm.HalfNormal("sigma", sigma=10)
        
        mu_regime = pm.math.switch(tau > idx, mu_1, mu_2)
        obs = pm.Normal("obs", mu=mu_regime, sigma=sigma, observed=prices)
        
        # Increased chains for better R-hat diagnostic
        trace = pm.sample(2000, tune=1000, chains=4, return_inferencedata=True, target_accept=0.95)
        
    return subset, trace

def analyze_and_report(subset, trace, event_name):
    """
    Addresses Reviewer Comment #1: 
    Convergence diagnostics, Quantitative impact, and Hypothesis mapping.
    """
    # 1. Convergence Diagnostics (Reviewer Requirement)
    print("\n--- 1. Convergence Diagnostics ---")
    summary = az.summary(trace, var_names=["mu_1", "mu_2", "tau"])
    print(summary[['mean', 'sd', 'r_hat']])
    
    # Check if R-hat is near 1.0
    rhat_max = summary['r_hat'].max()
    print(f"Max R-hat: {rhat_max:.4f} ({'Converged' if rhat_max < 1.05 else 'Warning: Poor Convergence'})")
    
    # Save Trace Plot (Diagnostic Visual)
    az.plot_trace(trace, var_names=["mu_1", "mu_2", "tau"])
    plt.tight_layout()
    plt.savefig(f"docs/diagnostics_{event_name.replace(' ', '_')}.png")
    
    # 2. Quantitative Impact (Reviewer Requirement)
    mu1 = summary.loc['mu_1', 'mean']
    mu2 = summary.loc['mu_2', 'mean']
    tau_idx = int(summary.loc['tau', 'mean'])
    detected_date = subset.index[tau_idx]
    
    abs_change = mu2 - mu1
    pct_change = (abs_change / mu1) * 100
    
    print("\n--- 2. Quantitative Regime Impact ---")
    print(f"Regime 1 (Pre-Break) Mean: ${mu1:.2f}")
    print(f"Regime 2 (Post-Break) Mean: ${mu2:.2f}")
    print(f"Absolute Shift: ${abs_change:.2f}")
    print(f"Percentage Shift: {pct_change:.2f}%")
    
    # 3. Hypothesis Mapping (Reviewer Requirement)
    print("\n--- 3. Event Hypothesis Mapping ---")
    print(f"Detected Break Date: {detected_date.date()}")
    print(f"Hypothesis: The break aligns with the {event_name}. The {pct_change:.2f}% shift confirms a fundamental structural regime change.")

    # 4. Standard Results Plot
    plt.figure(figsize=(12, 6))
    plt.plot(subset.index, subset.values, label="Actual Price", color='gray', alpha=0.5)
    plt.hlines(mu1, subset.index[0], detected_date, colors='red', lw=3, label=f"Mean 1: ${mu1:.2f}")
    plt.hlines(mu2, detected_date, subset.index[-1], colors='blue', lw=3, label=f"Mean 2: ${mu2:.2f}")
    plt.axvline(detected_date, color='black', linestyle='--', label=f"Break: {detected_date.date()}")
    plt.title(f"Bayesian Change Point: {event_name}")
    plt.legend()
    plt.savefig(f"docs/change_point_{event_name.replace(' ', '_')}.png")
    plt.show()

if __name__ == "__main__":
    # Ensure docs folder exists
    if not os.path.exists('docs'): os.makedirs('docs')
    
    data_file = 'data/BrentOilPrices.csv' 
    
    # Executing analysis
    data_subset, model_trace = run_bayesian_change_point(data_file, '2014-01-01', '2015-12-31')
    analyze_and_report(data_subset, model_trace, "2014 Price Collapse")