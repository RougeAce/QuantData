import yfinance as yf
import pandas as pd
import main
import matplotlib.pyplot as plt


'''This will soon be the center of everything. It will be how the backend connects with the frontend. 
It will go to the proper files and directories to fufil requetss made by the front. It will handel 
error catching.'''

def get_something(Ticker, something):
    return Ticker.info[something]

def get_historical_data(ticker, keys, start_date, end_date, interval="1d", export=False):
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval, group_by="ticker", auto_adjust=True, prepost=True)
    df = pd.DataFrame()
    for key in keys:
        if key not in data.columns:
            raise ValueError(f"{key} not in available columns: {data.columns}")
        df[key] = data[key]
    if export==True:
        file_name = f"{ticker}_historical_data_for_.xlsx"  # name of the Excel file
        sheet_name = f"{start_date}-{end_date}"  # name of the sheet in the Excel file
        df.to_excel(file_name, sheet_name=sheet_name)

    return df


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

