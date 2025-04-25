import feedparser
import csv
from datetime import datetime

# Türkçe anahtar kelimeler
keywords = [
   
   "Turkey election",
    "Turkey president",
    "Erdogan",
    "coup attempt",
    "parliament Turkey",
    "Turkey protest",
    "Turkey central bank",
    "interest rate decision",
    "inflation Turkey",
    "currency crisis"
]

# 2019–2024 tarih aralığı
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 12, 31)

# CSV dosyası
with open('../data/raw/reuters_tr_politika.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Title', 'Source', 'Keyword'])

    for keyword in keywords:
        query = keyword.replace(" ", "+")
        rss_url = f"https://news.google.com/rss/search?q={query}+site:reuters.com&hl=tr&gl=TR&ceid=TR:tr"

        feed = feedparser.parse(rss_url)

        print(f"🔎 '{keyword}' için {len(feed.entries)} haber bulundu.")

        for entry in feed.entries:
            try:
                published = datetime(*entry.published_parsed[:6])
            except:
                continue

            if start_date <= published <= end_date:
                writer.writerow([published.date(), entry.title, 'Reuters', keyword])

print("✅ Reuters Türkçe siyasi haberleri başarıyla kaydedildi (2019–2024).")
