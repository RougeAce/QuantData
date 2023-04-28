import yfinance as yf
from BackEnd import main
from datetime import datetime
import pandas as pd
import numpy as np




# Gets the cloest options to the stirkes

def get_options(ticker,exp_date, Seperate = False):
    options = ticker.option_chain(exp_date)
    calls = options.calls
    puts = options.puts
    if Seperate == True:
        return calls, puts
    else:
        return options

def get_closet_strike(target_call, target_put, ticker, exp_date):

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





def calculate_options(*options):
    total_premiums = 0
    max_profit = 0
    max_loss = 0
    for option in options:
        expiration_date_str = option[6:12]
        expiration_date = datetime.strptime(convert_date_options(expiration_date_str), '%Y-%m-%d').date()
        option_data = yf.Ticker(option).option_chain(expiration_date.strftime('%Y-%m-%d'))
        option_calls = option_data.calls
        option_puts = option_data.puts
        target_strike = option_data.calls['strike'].mean()
        closest_call = option_calls.iloc[(option_calls['strike'] - target_strike).abs().argmin()]
        closest_put = option_puts.iloc[(option_puts['strike'] - target_strike).abs().argmin()]
        stock_price = yf.Ticker(option).history(period='1d')['Close'][0]
        call_profit = (stock_price - closest_call['strike']) * closest_call['lastPrice'] * 100
        put_profit = (closest_put['strike'] - stock_price) * closest_put['lastPrice'] * 100
        total_option_premium = closest_call['lastPrice'] + closest_put['lastPrice']
        total_premiums += total_option_premium
        total_option_profit = call_profit if closest_call['strike'] > stock_price else put_profit
        max_profit = float('inf') if closest_call['lastPrice'] == 0 else max(max_profit, total_option_profit)
        max_loss = closest_call['lastPrice'] * -100 if closest_call['lastPrice'] != 0 else closest_put['lastPrice'] * -100
        max_loss = min(max_loss, total_option_profit)
    return (max_profit, max_loss, total_premiums)

def convert_date_options(option): #230505
    #C = option['contractSymbol']
    C = option

    Y = str(C[4])
    R = str(C[5])
    M = str(C[6])
    M2 = str(C[7])
    D1 = str(C[8])
    D2 = str(C[9])

    YYYYMMDD = ("20" + Y + R + "-" + M + M2 + "-" + D1 + D2)
    return YYYYMMDD

SC, SP, BC, BP = iron_condor(main.get_ticker("AAPL"), 170, 166, 1000, "2023-05-05")





print(calculate_options(SC['contractSymbol'], SP['contractSymbol'], BC['contractSymbol'], BP['contractSymbol']))


































