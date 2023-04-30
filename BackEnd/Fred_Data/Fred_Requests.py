import pandas as pd
import FRED

def get_gdp(Update_Request = False):
    if Update_Request == True:
        FRED.update_GDP_Data()
    df = pd.read_csv('GDP.csv')
    return df

def get_reccesion_years(Update_Request = False):
    if Update_Request == True:
        FRED.update_Recession_Data()
    df = pd.read_csv('Recessions.csv')
    df = df[df['value'] != 0]
    return df

get_reccesion_years()
