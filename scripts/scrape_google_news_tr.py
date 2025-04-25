import feedparser
import csv
from datetime import datetime

# Turkish Keywords
keywords = [
    "Türkiye seçimi",
    "Erdoğan",
    "Merkez Bankası",
    "enflasyon",
    "faiz kararı",
    "döviz krizi",
    "protesto Türkiye",
    "kabine değişikliği",
    "askeri darbe girişimi"
]

# Date Range
start_date = datetime(2019, 1, 1)
end_date = datetime(2024, 12, 31)

# Create CSV file
with open('../data/raw/google_news_tr_politika.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Title', 'Source', 'Keyword'])

    for keyword in keywords:
        query = keyword.replace(" ", "+")
        rss_url = f"https://news.google.com/rss/search?q={query}&hl=tr&gl=TR&ceid=TR:tr"

        feed = feedparser.parse(rss_url)

        print(f"🔎 '{keyword}' için {len(feed.entries)} haber bulundu.")

        for entry in feed.entries:
            try:
                published = datetime(*entry.published_parsed[:6])
            except:
                continue

            if start_date <= published <= end_date:
                writer.writerow([published.date(), entry.title, 'Google News', keyword])

print("✅ Google News successfuly saved. (2019–2024).")
