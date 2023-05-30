import yfinance as yf


def data_available(ticker):
  print(yf.Ticker(ticker).info)
