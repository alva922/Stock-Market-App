# Stock-Market-App
Plotly Dash Technical Analysis Stock Market App
We deploy a Plotly Dash stock market app [1] in Python using the dashboard [2] of user-defined stock prices with popular technical indicators available in TA.
We download the live stock price via Yahoo Finance [3].
The entire workflow consists of the following 5 steps:

Step 1: Select a stock ticker symbol (NVDA) and retrieve stock data frame (df) from yfinance API at an interval of 1m

Step 2: Add Moving Averages (5day and 20day) to df and plot live share price

Step 3: Add Volume, MACD, and Stochastic Oscillator from TA

Step 4: Save our stock chart in HTML form, which means all the interactive features will be retained in the graph

Step 5: Implement the Plotly Dash app containing live NVDA stock prices with MA 5-15-50-200, Volume, RSI, and MACD.
  References
[1] Plotly Dash TA Stock Market App
https://wp.me/pdMwZd-7A3
[2] Python: Adding Features To Your Stock Market Dashboard With Plotly
https://medium.com/@jsteinb/python-adding-features-to-your-stock-market-dashboard-with-plotly-4208d8bc3bd5
[3] Download Financial Dataset Using Yahoo Finance in Python
https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/
