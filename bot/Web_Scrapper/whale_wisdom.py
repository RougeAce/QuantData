import requests

# Send a GET request to the Wikipedia page
url = 'https://whalewisdom.com/filer/portolan-capital-management-llc#tabholdings_tab_link'
response = requests.get(url)

# Save the HTML content to a file
with open('sp500.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

print("HTML file saved as 'sp500.html'.")
