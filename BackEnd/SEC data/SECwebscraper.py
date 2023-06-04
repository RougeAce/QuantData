import requests
from bs4 import BeautifulSoup

def get_cik(ticker):
    # Construct the URL for the SEC search page
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&owner=exclude&action=getcompany"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)



    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the CIK in the response
    cik_element = soup.find("span", class_="companyName").find("a")
    if cik_element is None:
        print(f"No CIK found for ticker '{ticker}'")
        return None

    cik = cik_element.text.strip()

    return cik

# Example usage
ticker = "AAPL"
cik = get_cik(ticker)

