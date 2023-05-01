import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from BackEnd import main
import indicators

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

# Import modules or define functions as necessary

def stock_deviations(ticker):
    df = indicators.get_net_change(main.get_ticker(ticker))

    export = input("Would you like to view it as a pyplot? (Y/N)")

    if export.lower() == "y":
        plt.plot(df, label=main.get_ticker(ticker).info['longName'])
        plt.show()

'''stock_net change shows the net change in stock. It is currently on V1 and will be
upgraded to V2 where the inputs will be unlimited and you can customize the period'''
def stock_net_change(period = '30d', *ticker):
    export = input("Would you like to view it as a pyplot? (Y/N)")
    if export == "Y":
        for i in ticker:
            df = indicators.get_net_change(main.get_ticker(ticker), time=period)
            plt.plot(df, label=main.get_ticker(ticker).info['longName'])

    else:
        raise TypeError('Speed up function by not running this')






