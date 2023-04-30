import pandas as pd

def get_gdp():
    df = pd.read_csv('CSV_Data/GDP.csv')
    print(df)

get_gdp()