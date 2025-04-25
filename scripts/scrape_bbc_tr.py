import feedparser
import csv
from datetime import datetime

# Anahtar kelimeler 
keywords = [
    "Turkey elections",
    "Erdogan",
    "central bank Turkey",
    "inflation Turkey",
    "Turkey protests",
    "interest rate Turkey",
    "currency crisis Turkey",
    "cabinet reshuffle",
    "coup attempt Turkey"
]

# Hedef tarih aralığı
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 12, 31)

# Dosyayı oluştur ve yaz
with open('../data/raw/bbc_en_politics.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Title', 'Source', 'Keyword'])

    for keyword in keywords:
        query = keyword.replace(" ", "+")
        rss_url = f"https://news.google.com/rss/search?q={query}+site:bbc.com/news&hl=en&gl=US&ceid=US:en"

        feed = feedparser.parse(rss_url)

        print(f"🔎 '{keyword}' için {len(feed.entries)} BBC haberi bulundu.")

        for entry in feed.entries:
            try:
                published = datetime(*entry.published_parsed[:6])
            except:
                continue

            if start_date <= published <= end_date:
                writer.writerow([published.date(), entry.title, 'BBC News', keyword])

print("✅ BBC İngilizce haberleri başarıyla kaydedildi (2019–2024).")
