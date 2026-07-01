
# Stock Revenue Dashboard

A Python project that extracts and visualizes historical stock price 
and revenue data for Tesla and GameStop to identify whether stock price 
movements reflect actual business performance or market speculation.

---

## What it does

- Fetches historical stock price data using yfinance
- Scrapes annual revenue data from macrotrends.net using BeautifulSoup
- Cleans and processes both datasets automatically
- Generates interactive dashboards comparing stock price vs revenue using Plotly

---

## Key Insight

GameStop's stock price spiked dramatically in 2021 due to Reddit's 
WallStreetBets short squeeze, while revenue was continuously declining 
every single year. This project visually proves that disconnect between 
market speculation and real business performance.

---

## Project Structure

```
stock-revenue-dashboard/
├── data_fetcher.py    → fetches stock data and scrapes revenue tables
├── visualizer.py      → builds interactive Plotly dashboards
├── main.py            → entry point, runs everything
└── requirements.txt   → required libraries
```

## How to Run

**Step 1 — Clone the repository**
```
git clone https://github.com/jaykhuman/stock-revenue-dashboard.git
cd stock-revenue-dashboard
```

**Step 2 — Create and activate virtual environment**

Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

**Step 3 — Install required libraries**
```
pip install -r requirements.txt
```

**Step 4 — Run the project**
```
python main.py
```

Two interactive dashboards will open in your browser automatically.

---

## Companies Analyzed

| Company | Ticker | Data Source |
|---------|--------|-------------|
|  Tesla  |  TSLA  | yfinance + macrotrends.net |
| GameStop |  GME  | yfinance + macrotrends.net |

---

## Built With

- Python 3
- yfinance
- BeautifulSoup4
- Pandas
- Plotly
