import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf 


tickerSymbol = 'AAPL'


tickerData = yf.Ticker(tickerSymbol)


tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-2-28')


plt.plot(tickerDf['Close'])
plt.title('Historical Close Price for ' + tickerSymbol)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()





