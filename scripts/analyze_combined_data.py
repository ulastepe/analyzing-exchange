import pandas as pd
import matplotlib.pyplot as plt

# 1. Read news and group by week
events = pd.read_csv('../data/processed/all_events.csv', parse_dates=['Date'])
events['Week'] = events['Date'].dt.to_period('W').apply(lambda r: r.start_time)
weekly_events = events.groupby('Week').size().reset_index(name='Event_Count')

# 2. Read Google Trends data and get weekly averages
trends = pd.read_csv('../data/raw/google_trends.csv', skiprows=1)
trends.rename(columns={trends.columns[0]: 'Date'}, inplace=True)
trends['Date'] = pd.to_datetime(trends['Date'], errors='coerce')
trends.dropna(subset=['Date'], inplace=True)
trends['Week'] = trends['Date'].dt.to_period('W').apply(lambda r: r.start_time)
weekly_trends = trends.groupby('Week').mean().reset_index()


usd = pd.read_csv('../data/raw/usd_try.csv')

# Convert date to datetime
usd['Date'] = pd.to_datetime(usd['Date'], errors='coerce')
usd.dropna(subset=['Date'], inplace=True)

# Clear numeric column
usd['USD_TRY'] = usd['USD_TRY'].astype(str).str.extract(r'(\d+\.\d+)')
usd['USD_TRY'] = pd.to_numeric(usd['USD_TRY'], errors='coerce')
usd.dropna(subset=['USD_TRY'], inplace=True)

# Group by week
usd['Week'] = usd['Date'].dt.to_period('W').apply(lambda r: r.start_time)
weekly_usd = usd.groupby('Week')['USD_TRY'].mean().reset_index()


gold = pd.read_csv('../data/raw/Gold_Prices.csv')

# Convert date
gold.rename(columns={'Tarih': 'Date'}, inplace=True)
gold['Date'] = pd.to_datetime(gold['Date'], errors='coerce')
gold.dropna(subset=['Date'], inplace=True)

# Clear the price 
gold['FİYAT'] = pd.to_numeric(gold['FİYAT'], errors='coerce')
gold.dropna(subset=['FİYAT'], inplace=True)

# Group by week
gold['Week'] = gold['Date'].dt.to_period('W').apply(lambda r: r.start_time)
weekly_gold = gold.groupby('Week')['FİYAT'].mean().reset_index()

merged = weekly_events.merge(weekly_trends, on='Week', how='outer')
merged = merged.merge(weekly_usd, on='Week', how='outer')
merged = merged.merge(weekly_gold, on='Week', how='outer')
merged.sort_values(by='Week', inplace=True)
merged = merged.sort_values(by='Week')
merged.to_csv('../data/processed/merged_analysis.csv', index=False)


print("✅ Data has been successfully merged and is ready for analysis.")
