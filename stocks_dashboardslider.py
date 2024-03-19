import os
os.chdir('YOURPATH')    # Set working directory YOURPATH
os. getcwd()
# Raw Package
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr

# Market Data 
import yfinance as yf

#Graphing/Visualization
import datetime as dt 
import plotly.graph_objs as go 

# Override Yahoo Finance 
yf.pdr_override()

# Create input field for our desired stock 
stock=input("Enter a stock ticker symbol: ")

# Retrieve stock data frame (df) from yfinance API at an interval of 1m 
df = yf.download(tickers=stock,period='1d',interval='1m')

# add Moving Averages (5day and 20day) to df 
df['MA5'] = df['Close'].rolling(window=5).mean()
df['MA20'] = df['Close'].rolling(window=20).mean()

df.tail()
# fig1
# Declare plotly figure (go)
fig=go.Figure()

fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'], name = 'market data'))

# Add 5-day Moving Average Trace
fig.add_trace(go.Scatter(x=df.index, 
                         y=df['MA5'], 
                         opacity=0.7, 
                         line=dict(color='blue', width=2), 
                         name='MA 5'))
# Add 20-day Moving Average Trace
fig.add_trace(go.Scatter(x=df.index, 
                         y=df['MA20'], 
                         opacity=0.7, 
                         line=dict(color='orange', width=2), 
                         name='MA 20'))

fig.update_layout(
    title= str(stock)+' Live Share Price:',
    yaxis_title='Stock Price (USD per Shares)')               

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.show()

#fig2

from ta.trend import MACD 
from ta.momentum import StochasticOscillator 
import plotly
from plotly.subplots import make_subplots
# MACD 
macd = MACD(close=df['Close'], 
            window_slow=26,
            window_fast=12, 
            window_sign=9)
# Stochastic
stoch = StochasticOscillator(high=df['High'],
                             close=df['Close'],
                             low=df['Low'],
                             window=14, 
                             smooth_window=3)

from IPython.core.display import display, HTML
display(HTML("<style>div.output_scroll { height: 100em; }</style>"))
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
# Declare plotly figure (go)
fig=go.Figure()
# add subplot properties when initializing fig variable ***don't forget to import plotly!!!***
fig = plotly.subplots.make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.01, row_heights=[0.5,0.1,0.2,0.2])
# Plot price data on the 1st subplot (using code from last article)
fig.add_trace(go.Candlestick(x=df.index, 
                 open=df['Open'],
                 high=df['High'],
                 low=df['Low'],
                 close=df['Close'], name='market data'))
fig.add_trace(go.Scatter(x=df.index,
                 y=df['MA5'],
                 opacity=0.7,
                 line=dict(color='blue', width=2),
                 name='MA 5'))
fig.add_trace(go.Scatter(x=df.index,
                 y=df['MA20'],
                 opacity=0.7,
                 line=dict(color='orange', width=2),
                 name='MA 20'))
# Plot volume trace on 2nd row in our figure
fig.add_trace(go.Bar(x=df.index, 
                     y=df['Volume']
                    ), row=2, col=1)
# Plot MACD trace on 3rd row
fig.add_trace(go.Bar(x=df.index, 
                     y=macd.macd_diff()
                    ), row=3, col=1)
fig.add_trace(go.Scatter(x=df.index,
                         y=macd.macd(),
                         line=dict(color='black', width=2)
                        ), row=3, col=1)
fig.add_trace(go.Scatter(x=df.index,
                         y=macd.macd_signal(),
                         line=dict(color='blue', width=1)
                        ), row=3, col=1)
# Plot stochastics trace on 4th row
fig.add_trace(go.Scatter(x=df.index,
                         y=stoch.stoch(),
                         line=dict(color='black', width=1)
                        ), row=4, col=1)
fig.add_trace(go.Scatter(x=df.index,
                         y=stoch.stoch_signal(),
                         line=dict(color='blue', width=1)
                        ), row=4, col=1)
# Plot volume trace on 2nd row
colors = ['green' if row['Open'] - row['Close'] >= 0 
          else 'red' for index, row in df.iterrows()]
fig.add_trace(go.Bar(x=df.index, 
                     y=df['Volume'],
                     marker_color=colors
                    ), row=2, col=1)
# Plot MACD trace on 3rd row
colors = ['green' if val >= 0 
          else 'red' for val in macd.macd_diff()]
fig.add_trace(go.Bar(x=df.index, 
                     y=macd.macd_diff(),
                     marker_color=colors
                    ), row=3, col=1)
# Update the layout by changing the figure size, hiding the legend and rangeslider
fig.update_layout(height=1000, width=1200, 
                  showlegend=False, 
                  xaxis_rangeslider_visible=False)
# update y-axis label
fig.update_yaxes(title_text="Price", row=1, col=1)
fig.update_yaxes(title_text="Volume", row=2, col=1)
fig.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)
fig.update_yaxes(title_text="Stoch", row=4, col=1)

#fig3

