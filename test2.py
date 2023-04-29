import yfinance as yf

current = yf.Ticker('GDP').info

print(current)