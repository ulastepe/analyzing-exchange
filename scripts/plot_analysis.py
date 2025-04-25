import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. Veriyi oku
df = pd.read_csv('../data/processed/merged_analysis.csv', parse_dates=['Week'])

# 2. zaman dizisi oluştur (2019'dan 2024'e kadar)
full_range = pd.date_range(start='2019-01-07', end='2024-01-01', freq='W-MON')

# 3. Week sütununu varsa index olarak ayarla
df.set_index('Week', inplace=True)

# 4. Eksik haftaları ekle
df = df.reindex(full_range)

# 5. İndeksi tekrar WEEK sütununa dönüştür
df.reset_index(inplace=True)
df.rename(columns={'index': 'WEEK'}, inplace=True)

# 6. Sütun adlarını temizle ve büyük harfe çevir
df.columns = df.columns.str.strip().str.upper()
df['FİYAT'] = pd.to_numeric(df['FİYAT'], errors='coerce')

# 7. EVENT_COUNT eksikse 0 yap
if 'EVENT_COUNT' not in df.columns:
    raise ValueError("'EVENT_COUNT' sütunu eksik, CSV'yi kontrol et.")
df['EVENT_COUNT'] = df['EVENT_COUNT'].fillna(0)


# 9. Grafik: Siyasi Olaylar + USD/TRY
plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df['WEEK'], df['EVENT_COUNT'], color='darkred', label='Political Events', linewidth=2)
ax2.plot(df['WEEK'], df['USD_TRY'], color='blue', linestyle='--', label='USD/TRY')

ax1.set_ylabel('Number of Political Events', color='darkred')
ax2.set_ylabel('USD/TRY', color='blue')
plt.title('Relation Between Political Events and USD/TRY')
ax1.set_xlabel('Week')
fig = plt.gcf()
fig.autofmt_xdate()
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.tight_layout()
plt.savefig('../data/processed/plot_event_vs_usd.png')
plt.show()

# Grafik: Aylık Olay Sayısı + Altın
# 1. Siyasi olaylar için AY sütunu (Week'ten)
df['AY_Olay'] = pd.to_datetime(df['WEEK']).dt.to_period('M').dt.to_timestamp()

# 2. Altın fiyatı için AY sütunu (Date'ten)
df['AY_Altin'] = pd.to_datetime(df['DATE']).dt.to_period('M').dt.to_timestamp()

# 3. Grupla
monthly_events = df.groupby('AY_Olay')['EVENT_COUNT'].sum().reset_index()
monthly_gold = df.groupby('AY_Altin')['FİYAT'].mean().reset_index()

# 4. Grafik
plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(monthly_events['AY_Olay'], monthly_events['EVENT_COUNT'], color='darkred', label='Political Events', linewidth=2)
ax2.plot(monthly_gold['AY_Altin'], monthly_gold['FİYAT'], color='gold', linestyle='--', label='Gold (TL)')

ax1.set_ylabel('Monthly Political Events', color='darkred')
ax2.set_ylabel('Gold (TL)', color='goldenrod')
plt.title('Monthly Political Events and Gold Price Relationship')
ax1.set_xlabel('Month')
fig = plt.gcf()
fig.autofmt_xdate()
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.tight_layout()
plt.savefig('../data/processed/plot_event_vs_gold_monthly.png')
plt.show()



# 11. Korelasyon Matrisini Hesapla

# Google Trends sütununu bul
trend_col = None
for col in df.columns:
    if col not in ['WEEK', 'EVENT_COUNT', 'USD_TRY', 'FİYAT'] and pd.api.types.is_numeric_dtype(df[col]):
        trend_col = col
        break

if trend_col is None:
    raise ValueError("Google Trends sütunu bulunamadı!")

# Korelasyon hesapla
correlation_df = df[['EVENT_COUNT', trend_col, 'USD_TRY', 'FİYAT']].dropna()
correlation_matrix = correlation_df.corr().round(2)

print("\n📊 Correlation Matrix:")
print(correlation_matrix)

# Isı haritası
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Political Events, Google Searches and Economic Indicators Correlation Matrix')
plt.tight_layout()
plt.savefig('../data/processed/correlation_heatmap.png')
plt.show()
