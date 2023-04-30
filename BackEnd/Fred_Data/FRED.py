import requests
import pandas as pd

# Set up API endpoint and parameters
url = 'https://api.stlouisfed.org/fred/series/observations'
params = {
    'series_id': 'GDP', # The series ID for US GDP
    'api_key': 'c77fb902ec44501e7dc34fb01c0bc435', # Replace YOUR_API_KEY with your FRED API key
    'file_type': 'json',
    'frequency': 'q' # Set frequency to quarterly
}

# Make the API request
response = requests.get(url, params=params)

# Convert JSON response to a DataFrame
data = pd.json_normalize(response.json()['observations'])
df = pd.DataFrame(data, columns=['date', 'value'])

# Save the DataFrame to a CSV file in a specific directory
output_path = '/Users/treydavidson/PycharmProjects/YFINANCE/CSV_Data/GDP.csv'
df.to_csv(output_path, index=False)

# Print the DataFrame
print(df)
