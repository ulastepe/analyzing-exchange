import pandas as pd
import glob

# Tüm haber CSV dosyalarını oku 
files = glob.glob('../data/raw/*_politika.csv')  # yalnızca *_politika.csv'leri al

# Boş liste oluştur
dataframes = []

# Tüm dosyaları birleştir
for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Hepsini tek bir DataFrame'de birleştir
combined = pd.concat(dataframes, ignore_index=True)

# Tarihleri datetime formatına çevir
combined['Date'] = pd.to_datetime(combined['Date'], errors='coerce')

# Null satırları temizle
combined.dropna(subset=['Date', 'Title'], inplace=True)

# Tarihe göre sırala
combined.sort_values(by='Date', inplace=True)

# CSV olarak kaydet
combined.to_csv('../data/processed/all_events.csv', index=False)

print("✅ Tüm haber verileri başarıyla birleştirildi → data/processed/all_events.csv")
