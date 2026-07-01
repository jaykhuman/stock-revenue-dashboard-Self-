# make_subplots → creates a grid layout where multiple graphs can live together
from plotly.subplots import make_subplots
# (go) → this is what actually draws each individual line graph
import plotly.graph_objects as go
import os




os.makedirs('output/dashboards', exist_ok=True)

def make_dashboard(stock, revenue, company_name):
    '''
    1. make_subplots → create grid
    2. add_trace → stock price in row 1
    3. add_trace → revenue in row 2
    4. update_layout → main title
    5. update_xaxes/update_yaxes → axis labels
    6. write_html → save dashboard file
    '''

    fig = make_subplots(rows=2, cols= 1, subplot_titles=('Stock Price', 'Revenue'))
    #Despite the name "Scatter," this is Plotly's general tool for drawing line graphs too
    #fig.add_trace(...) → adds this graph onto our dashboard
    fig.add_trace(go.Scatter(x=stock['Date'], y=stock['Close'], name='Stock Price'),row=1, col=1)
    fig.add_trace(go.Scatter(x = revenue['Year'], y = revenue['Revenue'], name = 'Revenue'), row=2, col= 1)

    fig.update_layout(title = company_name)
    fig.update_xaxes(title_text = 'Data', row=1, col=1)
    fig.update_xaxes(title_text = 'Year', row=2, col=1)
    fig.update_yaxes(title_text = 'Price (USD)', row=1, col=1)
    fig.update_yaxes(title_text = 'Revenue (Millions)', row=2, col=1)

    fig.write_html(f'output/dashboards/{company_name}_dashboard.html')
    fig.show()