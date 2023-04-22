import yfinance as yf
import matplotlib.pyplot as plt


def current_share_price(Ticker):  # Gets the current share price from the market
    output = Ticker.info['marketCap'] / Ticker.info['sharesOutstanding']
    return output


def CIP(Ticker, Ticker2):  # Gets the shareprice over a certain period of time. Comapres two
    T1 = yf.Ticker(Ticker)
    T2 = yf.Ticker(Ticker2)
    TH = T1.history(period="1mo")['Open']
    T2H = T2.history(period="1mo")['Open']
    Export = input("Y/N Would you like to view it as a pyplot")
    if Export == "Y":
        # plot the opening price history for Ticker
        plt.plot(TH, label=Ticker)

        # plot the opening price history for Ticker2
        plt.plot(T2H, label=Ticker2)

        plt.show()
    else:
        pass


def get_ticker():
    ticker = input("Enter a ticker symbol: ")
    return ticker.upper()


# get all stock info
print(CIP(get_ticker(), get_ticker()))






