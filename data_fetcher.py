import requests
import pandas as pd
import io
import yfinance as yf

#only job is downloading the page
def get_html_page(url):
    # → pretends our Python script is a real browser, so the website doesn't block us
    headers = {'User-Agent' : 'Mozilla/5.0'}
    # goes to that URL and downloads the page, pretending to be a browser
    response = requests.get(url, headers = headers)

    return response.text

def get_revenue_table(tables):
    for table in tables:
        if 'Annual Revenue' in table.text:
            #properly converts the matched HTML table into a clean DataFrame
            table = pd.read_html(io.StringIO(str(table)))[0]
            table.columns = ['Year', 'Revenue']
            table['Revenue'] = table['Revenue'].str.replace('$', '').str.replace(',', '').astype(float)
            return table

def get_stock_data(ticker_symbol):
    # Take a ticker symbol like "TSLA" or "GME", fetch its full historical stock price data
    ticker = yf.Ticker(ticker_symbol)
    stock = ticker.history(period = 'max')
    stock.reset_index(inplace=True)
    return stock