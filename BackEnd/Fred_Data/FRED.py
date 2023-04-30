import pandas as pd
import PASSWORD
import requests

def get_fred_data(freq, pull_data='USREC', update=True, R=True):
    if update == False and R == False:
        raise TypeError('Both update and request return are false')
    # Set up API endpoint and parameters
    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': pull_data,
        'api_key': PASSWORD.API_KEY,
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
            df.to_csv(pull_data + '.csv', index=False)

        if R:
            return df

    except requests.exceptions.HTTPError as e:
        return f"Request error: {e.response.text}"

def get_gdp(freq = 'q', Update = True, R = True):
    return get_fred_data(freq, pull_data='GDP', Update = Update, R = R)

def get_reccesion(freq = 'm', Update = True, R = True):
    return get_fred_data(freq, pull_data="USREC", update = Update, R=R)




