import pandas as pd
import glob

# Read all CSV news 
files = glob.glob('../data/raw/*_politika.csv')  # yalnızca *_politika.csv'leri al

# Create an empty list
dataframes = []

# Merge all files
for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine them all into one DataFrame
combined = pd.concat(dataframes, ignore_index=True)

# Convert dates to datetime format
combined['Date'] = pd.to_datetime(combined['Date'], errors='coerce')

# Clear the nulls
combined.dropna(subset=['Date', 'Title'], inplace=True)

# Sorted by Date
combined.sort_values(by='Date', inplace=True)

# Save as CSV
combined.to_csv('../data/processed/all_events.csv', index=False)

print("✅ All news data has been successfully merged → data/processed/all_events.csv")
