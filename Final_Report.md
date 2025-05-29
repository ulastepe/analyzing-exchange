# Final Report – How Political Events and Google Searches Affect Economic Indicators in Turkey (2019–2024)
*Erkan Ulaş Tepe*

---

## 1. Motivation

In a politically dynamic and economically sensitive country like Turkey, understanding the relationship between political developments, public attention, and market outcomes is essential. This project explores whether political events and shifts in public interest—as reflected by Google search behavior—can influence major economic indicators such as the USD/TRY exchange rate and gold prices. As someone interested in both data science and economic trends, I aimed to reveal patterns that could be valuable for investors, policy-makers, and researchers.

---

## 2. Data Sources

Three primary categories of data were used:

- **Economic Data:**
  - USD/TRY exchange rates and gold prices from:
    - Central Bank of Turkey (EVDS)
    - Yahoo Finance

- **Public Search Interest (Google Trends):**
  - Keywords: “dolar kuru”, “altın fiyatı”, “seçim”, “siyasi”, “zam”
  - Weekly normalized search volume for Turkey

- **Political Events:**
  - Manually labeled significant political dates between 2019 and 2024
  - Sources: Reuters, BBC News

All data was merged into a unified weekly dataset. Missing values were addressed using forward-fill and median imputation techniques.

---

## 3. Data Analysis

### 3.1 Exploratory Data Analysis (EDA)

- Time-series plots revealed consistent spikes in USD/TRY and gold prices following major political events.
- Google searches for “dolar kuru” and “altın fiyatı” tended to rise in advance of or during these events.
- Correlation matrices and lag analysis confirmed strong positive associations between search trends and economic indicators, especially for the exchange rate.

### 3.2 Hypothesis Testing

Two hypotheses were tested:

- **H₁:** Political event weeks significantly affect the USD/TRY exchange rate.
- **H₂:** Google search spikes significantly affect gold prices.

In both cases, t-tests resulted in **p-values < 0.05**, indicating statistically significant differences in economic indicator behavior during political event windows.

---

### 3.3 Machine Learning Models

To assess predictive capability, three machine learning models were tested on both indicators.

#### a) Gold Price Regression(0.2 Train Size)

| Model                     | R² Score |
|---------------------------|----------|
| K-Nearest Neighbors (k=5) | 0.9876   |
| Decision Tree             | 0.9772   |
| Random Forest             | **0.9920** |

- The **Random Forest** model performed best, capturing over 99% of the variance in gold prices.
- KNN provided good performance with minimal tuning.
- Decision Trees, while interpretable, were slightly less accurate.

#### b) USD/TRY Exchange Rate Regression(0.2 Train Size)

| Model                     | R² Score |
|---------------------------|----------|
| K-Nearest Neighbors (k=5) | 0.9959   |
| Decision Tree             | 0.9984   |
| Random Forest             | **0.9989** |

- Exchange rate predictions were remarkably accurate across all models.
- The **Random Forest** model again offered the best performance with an **R² of 0.9989**.
- This suggests strong, predictable relationships between public attention and exchange rate movements.

#### Feature Importance (Random Forest)

- **Top Features:**
  - Google Trends search terms (“dolar kuru”, “altın fiyatı”)
  - Political event count
  - Lagged prices
- Exchange rate was especially sensitive to the political calendar and public concern reflected in searches.

---

## 4. Findings

- Political events have a **strong and measurable impact** on USD/TRY exchange rates.
- **Google search behavior is predictive**, with notable interest spikes occurring shortly before economic shifts.
- Gold prices are also affected, though with **slightly weaker correlations** and more global influence.
- **Machine learning models validated these insights** with high R² values, especially for USD/TRY.

---

## 5. Limitations and Future Work

### Limitations
- The dataset is limited to Turkey; results may not generalize.
- Sentiment analysis of the political news headlines was not included.
- Google Trends provides **normalized, not absolute** search data.

### Future Plans
- Add sentiment analysis to understand tone (positive/negative) of political headlines.
- Expand to other countries for comparative studies.
- Expand the date line for more data.

---

## 6. Conclusion

The analysis shows that both political events and public search interest **significantly influence Turkey’s economic indicators**, especially the USD/TRY exchange rate. The public reacts swiftly to uncertainty, and this behavior is detectable through digital traces like search queries. Predictive models not only confirm these relationships but also offer a framework for anticipating economic shifts. This project demonstrates the power of combining behavioral and financial data to understand macroeconomic dynamics.
