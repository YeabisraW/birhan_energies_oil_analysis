import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model

# 1. Load data
df = pd.read_csv('data/BrentOilPrices.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format='mixed')
df.set_index('Date', inplace=True)

# 2. Calculate Daily Returns (This is what we model for volatility)
# We multiply by 100 to make the numbers easier for the model to "see"
df['Returns'] = 100 * df['Price'].pct_change().dropna()
returns = df['Returns'].dropna()

# 3. Define the GARCH(1, 1) model
# 'vol'='Garch', 'p'=1, 'q'=1 is the standard "gold record" for finance
model = arch_model(returns, vol='Garch', p=1, q=1)
model_fit = model.fit(disp='off')

# 4. Extract Conditional Volatility
df['Volatility'] = model_fit.conditional_volatility

# 5. Visualization
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Volatility'], color='orange', label='GARCH Volatility (Risk)')
plt.title('Brent Oil Market Risk Over Time (GARCH Model)')
plt.ylabel('Volatility')
plt.legend()
plt.grid(alpha=0.3)

# Save the plot for the final report
plt.savefig('docs/garch_volatility.png')
plt.show()

print(model_fit.summary())