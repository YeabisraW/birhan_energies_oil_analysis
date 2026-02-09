import pandas as pd

# Creating a comprehensive list of events impacting Brent Oil
events = [
    {"Date": "1990-08-02", "Event": "Invasion of Kuwait", "Type": "Conflict"},
    {"Date": "1991-01-17", "Event": "Operation Desert Storm", "Type": "Conflict"},
    {"Date": "1997-07-01", "Event": "Asian Financial Crisis", "Type": "Economic"},
    {"Date": "2001-09-11", "Event": "9/11 Attacks", "Type": "Geopolitical"},
    {"Date": "2003-03-20", "Event": "Iraq War Start", "Type": "Conflict"},
    {"Date": "2008-07-11", "Event": "Global Financial Crisis Peak", "Type": "Economic"},
    {"Date": "2011-02-15", "Event": "Libyan Civil War / Arab Spring", "Type": "Geopolitical"},
    {"Date": "2014-11-27", "Event": "OPEC Thanksgiving Policy Shift", "Type": "Policy"},
    {"Date": "2016-11-30", "Event": "OPEC+ Formation (Vienna)", "Type": "Policy"},
    {"Date": "2018-05-08", "Event": "US Withdrawal from JCPOA (Iran)", "Type": "Sanctions"},
    {"Date": "2020-03-06", "Event": "Russia-Saudi Price War", "Type": "Policy"},
    {"Date": "2020-04-20", "Event": "COVID-19 Negative Demand Shock", "Type": "Economic"},
    {"Date": "2021-03-23", "Event": "Ever Given Suez Canal Blockage", "Type": "Logistics"},
    {"Date": "2022-02-24", "Event": "Russia-Ukraine War", "Type": "Conflict"},
    {"Date": "2022-05-30", "Event": "EU Embargo on Russian Oil", "Type": "Sanctions"}
]

df_events = pd.DataFrame(events)
df_events['Date'] = pd.to_datetime(df_events['Date'])

# Save to your 'data' folder
df_events.to_csv('data/oil_events.csv', index=False)
print("Event Ledger saved to data/oil_events.csv")