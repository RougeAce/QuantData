from BackEnd.FrontEnd.CLI.CLI_Testing_Features import main
import pandas as pd
import csv

def buy(ticker,amount = 1, price_target = None):
    if price_target == None:
        price_share = main.current_share_price(main.get_ticker(ticker))
        total_price = amount * price_share


def update_book(name, amount, B = True):
    df = pd.read_csv('Manager.csv ')
    if B:
        value = df.iloc[0, 1]
        value -= amount
        df.iloc[0, 1] = value
        if name in df['Asset'].values:
            index1 = df.loc[df['Asset'] == name].index[0]
            value = df.iloc[index1, 1]
            value += amount
            df.iloc[index1, 1] = value
            df.to_csv('Manager.csv ', index=False)
        else:
            with open('Manager.csv ', 'a') as file:
                writer = csv.writer(file)
                new_row = [name, amount]
                writer.writerow(new_row)


    if B == False:
        # Adds the cash value and subracts the amount thats being sold
        value = df.iloc[0, 1]
        value += amount
        df.iloc[0, 1] = value
       #
        index = df.loc[df['Asset'] == name].index[0]
        value = df.iloc[index, 1]
        value -= amount
        df.iloc[index, 1] = value
        df.to_csv('Manager.csv ', index=False)


update_book("AAPL", 10000, True)
