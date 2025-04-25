# DSA 210 - Project Proposal Report

## Title

How Political Events and Google Searches Affect Economic Indicators

## Introduction

I chose this topic because I am curious about whether political events and people's interests (shown by Google searches) can change economic indicators such as exchange rates, interest rates, and gold prices. I believe this analysis can help in understanding how news and public attention might affect the economy. In addition, I am an also investor to exchange rates so my motivation on this project to get a efficient knowlenge and being able to use it.

Research Question & Hypothesis

Research Question: How do political events and Google search trends influence economic indicators such as exchange rates, interest rates, and gold prices?

Hypothesis: I believe that significant political events and increased public attention (reflected through increased Google searches) directly cause noticeable fluctuations in economic indicators such as exchange rates, interest rates, and gold prices, as people react quickly to uncertainty and major news events.

Time Frame

I will analyze data from the last 5 years (2019-2024), focusing especially on periods around major elections and key political events.

## Data Sources

I plan to use data from the following sources:

- **Economic Data:**
  - Central Bank of Turkey (https://evds2.tcmb.gov.tr/)
  - Investing.com (https://www.investing.com)
  - Yahoo Finance (https://finance.yahoo.com/)

- **Political News:**
  - Reuters (https://www.reuters.com/)
  - BBC News (https://www.bbc.com/news)
  - Google News (https://news.google.com/)

- **Google Search Trends:**
  - Google Trends (https://trends.google.com/)


## Methodology

### Data Collection

- **Economic indicators:**
  - I will collect data about exchange rates, interest rates, and gold prices by downloading it from official websites like the Central Bank of Turkey and Yahoo Finance. If necessary, I may use Python scripts to scrape additional data from Investing.com.

- **Political news:**
  - I will gather news headlines from websites like Reuters, BBC News, and Google News using simple Python scraping methods. Afterwards, I will conduct basic sentiment analysis to see if the news was mostly positive or negative.

- **Google Trends:**
  - I will collect search volume data from Google Trends by choosing relevant keywords related to economics and politics.

### Data Analysis

- First, I will perform exploratory data analysis using charts and graphs.
- Next, I will use sentiment analysis techniques on political news to check the tone of the headlines.
- Then, I will run simple statistical tests and check for correlations.

## Expected Results

I expect to find connections between political events and Google searches with economic indicators like exchange rates or gold prices. For example, I expect to see changes in economic indicators after major political announcements or events.

## Limitations

There are a few limitations in this project:
- Sentiment analysis might not always accurately capture the true feelings from news headlines.
- There could be problems or missing data when collecting information from some sources.

## Future Work

In the future, I can expand my project to include:
- More countries or a longer time period.
- Additional data sources, such as social media, to improve the accuracy of my analysis.

## Visualizations & Captions

### Figure 1: Relation Between Political Events and USD/TRY
![USD vs Events](data/processed/plot_event_vs_usd.png)

* This time-series plot overlays weekly political events (solid red) with USD/TRY (blue dashed).
* From 2019–2021, events stay low while the dollar climbs steadily.
* Beginning mid-2021 (especially mid-2023), spikes in events align with sudden USD/TRY jumps, suggesting heightened political activity accelerates depreciation.

---

### Figure 2: Monthly Political Events and Gold Price Relationship
![Monthly Events vs Gold](data/processed/plot_event_vs_gold_monthly.png)

* Monthly totals of political events (solid red) are paired with average gold price (yellow dashed).
* Months with pronounced event peaks (e.g., May 2022, Spring 2023) correspond to significant gold price jumps.
* This suggests gold acts as a “safe haven”: during political volatility, demand (and price) spikes sharply.

---

### Figure 3: Correlation Matrix of Events, Searches & Economic Indicators
![Correlation Heatmap](data/processed/correlation_heatmap.png)

* **Event count vs. gold searches:** ~0.52 (moderate positive).  
* **Event count vs. USD/TRY:** ~0.09 (weak overall).  
* **Gold searches vs. USD/TRY:** ~0.59 (solid positive).  
* **USD/TRY vs. gold price:** ~0.99 (near-perfect co-movement).

---


## Author

- Name: Erkan Ulaş Tepe


