import yfinance as yf

ticker = yf.Ticker('AAPL')
earnings_keys = ticker.earnings.keys()

print(earnings_keys)
