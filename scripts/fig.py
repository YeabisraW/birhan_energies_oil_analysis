import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv('data/BrentOilPrices.csv')

# 2. Convert Date column to datetime objects (Essential for time series)
# If your dates are like '20-May-87', pandas handles this automatically
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 3. Create the Visualization
plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='Date', y='Price', color='#3182ce', linewidth=1.5)

# 4. Add "Regime" Labels (Addressing the Reviewer's demand for context)
events = {
    '2008-07-01': 'Financial Crisis',
    '2014-11-01': 'OPEC Non-Cut',
    '2020-04-01': 'COVID-19',
    '2022-02-24': 'Ukraine Invasion'
}

for date, label in events.items():
    plt.axvline(pd.to_datetime(date), color='red', linestyle='--', alpha=0.5)
    plt.text(pd.to_datetime(date), df['Price'].max(), label, rotation=90, verticalalignment='top')

# 5. Professional Formatting
plt.title('Figure 1: Historical Brent Oil Price Trend (1987–2022)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price (USD per Barrel)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.tight_layout()

# 6. Save for Report
plt.savefig('brent_price_trend.png', dpi=300)
plt.show()