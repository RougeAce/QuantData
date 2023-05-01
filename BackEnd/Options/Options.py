import yfinance as yf
import pandas as pd
import numpy as np
from BackEnd import main
import test
import csv


def get_options(ticker,exp_date, Seperate = False):
    options = ticker.option_chain(exp_date)
    calls = options.calls
    puts = options.puts
    if Seperate == True:
        return calls, puts
    else:
        return options

def get_closet_strike(target_call, target_put, ticker, exp_date):
    if isinstance(ticker, yf.Ticker) == False:
        ticker = main.get_ticker(ticker)

    calls, puts = get_options(ticker, exp_date, True)

    df_calls = pd.DataFrame(calls)
    df_puts = pd.DataFrame(puts)
    diff_calls = abs(df_calls['strike'] - target_call)
    diff_puts = abs(df_puts['strike'] - target_put)


    # Find index of minimum absolute difference
    min_idx_calls = np.argmin(diff_calls)
    min_idx_puts = np.argmin(diff_puts)

    # Get corresponding strike prices

    return df_calls.loc[min_idx_calls], df_puts.loc[min_idx_puts]

def iron_condor(ticker, HStrike, LStrike, Max_Loss, exp):

    optionHigh, optionLow = get_closet_strike(HStrike, LStrike, ticker, exp)


    TP = optionHigh['lastPrice'] + optionLow['lastPrice']

    # Assigens them a position

    df_calls, df_puts = get_options(ticker, exp, True)

    # Gets rid of all the ones we are not considering
    df_calls = df_calls[df_calls['strike'] > optionHigh['strike']]
    df_puts = df_puts[df_puts['strike'] < optionLow['strike']]

    # Initialize closest call and put to None
    closest_call = None
    closest_put = None

    for index, row in df_calls.iterrows():
        strike = row['strike']
        diff_price = strike - optionHigh['strike']
        diff_p = optionHigh['lastPrice'] - row['lastPrice']
        max_loss = (diff_price * 100) - diff_p
        diff_Max = abs(Max_Loss - max_loss)

        # Update closest_call if it's the first iteration
        if closest_call is None:
            closest_call = row
        else:
            if diff_Max < abs(closest_call['lastPrice'] - optionHigh['lastPrice']):
                closest_call = row

    for index, row in df_puts.iterrows():
        strike = row['strike']
        diff_strike = optionLow['strike'] - strike
        diff_p = optionHigh['lastPrice'] - row['lastPrice']
        max_loss = (diff_strike * 100) - diff_p
        diff_Max = abs(Max_Loss - max_loss)

        # Update closest_put if it's the first iteration
        if closest_put is None:
            closest_put = row
        else:
            if diff_Max < abs(closest_put['lastPrice'] - optionHigh['lastPrice']):
                closest_put = row

    # Print closest call and put option contracts
    return  optionHigh, optionLow, closest_call, closest_put

SC, SP, BC, BP = iron_condor(yf.Ticker("AAPL"), 170, 166, 500, "2023-05-05")



max_loss, max_gain, net_premiums = test.calculate_options(SC['contractSymbol'] + "S", SP['contractSymbol'] + "S", BC['contractSymbol'] + "B", BP['contractSymbol'] + "B")
print(f"Max Loss = {max_loss}")









