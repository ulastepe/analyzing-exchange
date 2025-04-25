import pandas as pd
import matplotlib.pyplot as plt

# Read Google Trends data
trends = pd.read_csv('../data/raw/google_trends.csv', skiprows=1)

# Name the first column as Date
trends.rename(columns={trends.columns[0]: 'Date'}, inplace=True)

# Convert to date format
trends['Date'] = pd.to_datetime(trends['Date'])

# Graph
plt.figure(figsize=(14, 6))
for column in trends.columns[1:]:
    plt.plot(trends['Date'], trends[column], label=column)

plt.title('Google Arama Trendleri (2019–2024)')
plt.xlabel('Tarih')
plt.ylabel('İlgi Düzeyi (0-100)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
