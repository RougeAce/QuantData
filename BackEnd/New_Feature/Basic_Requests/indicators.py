import pandas as pd
import yfinance as yf
from BackEnd import main
def get_net_change(ticker, time='30d'):
    # Define or import the get_net_change() function here
    history = ticker.history(period=time)
    net_change = (history["Close"] - history["Open"]) / history["Open"] * 100
    return pd.DataFrame({"Net Change": net_change})





