import requests
import pandas as pd
import PASSWORD

# Set up API endpoint and parameters



def update_GDP_Data():
    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': 'GDP', # The series ID for US GDP
        'api_key': PASSWORD.API_KEY, # Replace YOUR_API_KEY with your FRED API key
        'file_type': 'json',
        'frequency': 'q' # Set frequency to quarterly
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Convert JSON response to a DataFrame
    data = pd.json_normalize(response.json()['observations'])
    df = pd.DataFrame(data, columns=['date', 'value'])

    # Save the DataFrame to a CSV file in a specific directory
    output_path = 'GDP.csv'
    df.to_csv(output_path, index=False)

def update_Recession_Data():
    # Set up API endpoint and parameters
    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': 'USREC',  # The series ID for US recession data
        'api_key': PASSWORD.API_KEY,  # Replace YOUR_API_KEY with your FRED API key
        'file_type': 'json'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Convert the API response to a pandas DataFrame
    data = response.json()['observations']
    df = pd.DataFrame.from_records(data, columns=['realtime_start', 'realtime_end', 'date', 'value'])

    # Save the DataFrame to a CSV file
    df.to_csv('Recessions.csv', index=False)

update_Recession_Data()