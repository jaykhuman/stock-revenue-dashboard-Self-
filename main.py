from bs4 import BeautifulSoup
from data_fetcher import get_html_page, get_revenue_table, get_stock_data
from visualizer import make_dashboard


tesla_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

tesla_html = get_html_page(tesla_url)
tesla_soup = BeautifulSoup(tesla_html, 'html.parser')
tesla_revenue = get_revenue_table(tesla_soup)
tesla_stock = get_stock_data('TSLA')
# print(tesla_stock.head())
# print(tesla_revenue.head())
make_dashboard(tesla_stock, tesla_revenue, 'Tesla')


print('-' * 70)

gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

gme_html = get_html_page(gme_url)
gamestop_soup = BeautifulSoup(gme_html, 'html.parser')
gamestop_revenue = get_revenue_table(gamestop_soup)
gme_stock = get_stock_data('GME')
# print(gme_stock.head())
# print(gamestop_revenue.head())
make_dashboard(gme_stock, gamestop_revenue, 'GameStop')