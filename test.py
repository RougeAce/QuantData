import yfinance as yf
ticker = "AAPL"

T = yf.Ticker(ticker)

print(T.history(period="1mo")['Open'])

