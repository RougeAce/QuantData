import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from BackEnd import main

''' This may be implemented curretly in testing
def compare_stocks(period = '1mo', *stocks):
    Export = input('Y/N Would you like to view it as a pyplot')
    for i in stocks:
        A = i.history(period=period)['Open']
        if Export == 'Y':
            plt.plot(A, label = i.info['longName'])

    plt.legend()

    plt.show()'''



def compare_stock_prices(period='1mo'):
    num_tickers = int(input("Enter the number of tickers to compare: "))
    tickers = []
    for i in range(num_tickers):
        symbol = input("Enter ticker symbol: ")
        ticker = yf.Ticker(symbol)
        tickers.append(ticker)

    export = input("Would you like to view it as a pyplot (Y/N)? ")
    if export.upper() == "Y":
        for i in tickers:
            data = i.history(period=period)['Open']
            name = i.info['longName']
            plt.plot(data, label=name)

        plt.legend()
        plt.show()
    else:
        for i in tickers:
            data = i.history(period=period)['Open']
            name = i.info['longName']
            print(name)
            print(data)


def CIP(Ticker, Ticker2):  # Gets the shareprice over a certain period of time.
    T1 = Ticker.history(period="1mo")['Open']
    T2 = Ticker2.history(period="1mo")['Open']
    Export = input("Y/N Would you like to view it as a pyplot")
    if Export == "Y":
            # plot the opening price history for Ticker
            plt.plot(T1, label=Ticker)

            # plot the opening price history for Ticker2
            plt.plot(T2, label=Ticker2)

            plt.show()
    else:
        pass

compare_stock_prices('1mo')