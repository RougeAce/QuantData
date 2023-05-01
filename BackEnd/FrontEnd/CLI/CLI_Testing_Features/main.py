import yfinance as yf
import matplotlib.pyplot as plt


'''This will soon be the center of everything. It will be how the backend connects with the frontend. 
It will go to the proper files and directories to fufil requetss made by the front. It will handel 
error catching.'''

def current_share_price(Ticker):  # Gets the current share price from the market
    output = Ticker.info['currentPrice']
    return round(output, 4)

def previous_close_price(Ticker):
    output = Ticker.info['previousClose']
    return round(output, 4)


def ticker_name(Ticker):
    output = Ticker.info['longName']
    return output

def get_ticker(symbol = None):
    if symbol == None:
        symbol = input("Enter a ticker symbol: ")
    else:
        symbol = symbol

    ticker = yf.Ticker(symbol.upper())
    return ticker












