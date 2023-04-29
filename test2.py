import yfinance as yf

current = yf.Ticker('AAPL230505C00172500').info

print(current)