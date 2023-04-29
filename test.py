import yfinance as yf

from BackEnd import main
from datetime import datetime
import pandas as pd
import numpy as np

import yfinance as yf


def calculate_options(*options):
    max_loss = 0
    max_gain = 0
    net_premiums = 0

    # Keeps track of the number of puts and calls sold and bought
    CS = 0
    CB = 0
    PS = 0
    PB = 0


    for option in options:
        bought_or_sold = option[-1]
        option_type = option[10]
        current = option[:-1]
        current = yf.Ticker(current)
        try:
            Price = current.info['lastPrice']
        except (TypeError, KeyError):
            Price = (current.info['bid'] + current.info['ask']) / 2

        if option_type == "C":
            if bought_or_sold == "B":
                CB += 1
                net_premiums -= Price
                max_loss += Price
                max_gain += float('inf')
            elif bought_or_sold == "S":
                CS += 1
                net_premiums += Price
                max_loss += float('inf')
                max_gain += Price
            else:
                raise TypeError("Invalid option transaction. Can't determine if bought or sold.")
        elif option_type == "P":
            if bought_or_sold == "B":
                PB += 1
                net_premiums -= Price
                max_loss += Price
                max_gain += float('inf')
            elif bought_or_sold == "S":
                PS += 1
                net_premiums += Price
                max_loss += float('inf')
                max_gain += Price
            else:
                raise TypeError("Invalid option transaction. Can't determine if bought or sold.")
        else:
            raise TypeError("Invalid option type. Must be 'CALL' or 'PUT'.")


    if CS == 1 and CB == 1 and PS == 1 and PB == 1:
        max_loss = net_premiums
        max_gain = net_premiums
    elif CS == 1 and CB == 1:
        max_loss = net_premiums - Price
        max_gain = Price - net_premiums
    elif PS == 1 and PB == 1:
        max_loss = Price - net_premiums
        max_gain = net_premiums - Price
    else:
        raise TypeError("Invalid combination of options. Must be Iron Butterfly or Iron Condor.")



    return max_loss, max_gain, net_premiums








































