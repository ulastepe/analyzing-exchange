import yfinance as yf
import pandas as pd

usd_try = yf.download('USDTRY=X', start='2019-01-01', end='2024-12-31')

usd_try = usd_try[['Close']].reset_index()
usd_try.rename(columns={'Close': 'USD_TRY'}, inplace=True)

# Save as csv
usd_try.to_csv('../data/raw/usd_try.csv', index=False)

print("USD/TRY verisi başarıyla kaydedildi.")




