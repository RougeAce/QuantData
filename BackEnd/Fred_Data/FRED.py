import pandas as pd
import PASSWORD
import requests

'''This file is used to pull Fred New_Feature. You need the sieries which can be find by looking up Fred and then the term you 
want. For example, GDP is at https://fred.stlouisfed.org/series/GDP. 
So GDP is the sieries ID or pull data in this form. '''

def get_fred_data(freq, pull_data='GDP', update=True, R=True, name = None):
    if name == None:
        name = pull_data
    if update == False and R == False:
        raise TypeError('Both update and request return are false')
    # Set up API endpoint and parameters
    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': pull_data,
        'api_key': PASSWORD.Fred_API_KEY,
        'file_type': 'json',
        'frequency': freq,
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Convert the API response to a pandas DataFrame
        data = response.json()['observations']
        df = pd.DataFrame.from_records(data, columns=['realtime_start', 'realtime_end', 'date', 'value'])



        if update:
            # Save the DataFrame to a CSV file
            df.to_csv('FREDCSV/' + name + '.csv', index=False)

        if R:
            return df

    except requests.exceptions.HTTPError as e:
        return f"Request error: {e.response.text}"

def get_gdp(freq = 'q', Update = True, R = True):
    return get_fred_data(freq, pull_data='GDP', update = Update, R = R, name = "US|GDP")

def get_reccesion(freq = 'm', Update = True, R = True):
    return get_fred_data(freq, pull_data="USREC", update = Update, R=R, name = "US|Reccesions")

def get_M2(freq = 'm', Update = True, R = True):
    return get_fred_data(freq, pull_data='WM2NS', update= Update, R=R, name = "US|M2")

def get_inflation(freq ='m', Update = True, R = True):
    return get_fred_data(freq, pull_data='CPIAUCSL', update = Update, R = R, name = "US|CPI|Inflation")

def get_intrest_rates(freq = 'm', Update = True, R = True):
    return get_fred_data(freq, pull_data='DFF', update= Update, R = R, name = "US|IntrestRates")







