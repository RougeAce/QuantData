import requests

'''Pulls Cyrpto Data. Be careful not to abuse this as new API will be needed. '''
def get_crypto_pair(pair = 'BTC-USD'):
    # Set the API endpoint and symbol for Bitcoin on Coinbase
    endpoint = f'https://api.coinbase.com/v2/prices/{pair}/spot'
    symbol = pair

    # Send a GET request to the Coinbase API endpoint for the specified symbol
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the current Bitcoin price
        data = response.json()
        price = data['data']['amount']
        return price
    else:

        raise TypeError(f'The request was met with {response} instead of what we requested')

def get_pair():
    pair = input('What pair would you like to ')

print(get_crypto_pair(pair = 'BTC-USD'))

