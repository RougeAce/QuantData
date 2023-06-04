import requests
from bs4 import BeautifulSoup

def search_10k_filings(cik):
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-K"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table of 10-K filings
    table = soup.find("table", class_="tableFile2")

    # Extract the rows containing the filings
    rows = table.find_all("tr")[1:]  # Exclude header row

    # Extract relevant information from each row
    filings = []
    for row in rows:
        cells = row.find_all("td")
        filing_date = cells[3].text.strip()
        filing_type = cells[0].text.strip()
        filing_description = cells[1].text.strip()
        filing_link = cells[1].find("a")["href"]

        filing = {
            "date": filing_date,
            "type": filing_type,
            "description": filing_description,
            "link": filing_link
        }
        filings.append(filing)

    return filings

def extract_balance_sheet(filing_link):
    response = requests.get(filing_link)
    if response.status_code != 200:
        print(f"Error retrieving filing: {filing_link}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section containing the balance sheet information
    balance_sheet_section = soup.find("a", text="Consolidated Balance Sheets")
    if balance_sheet_section is None:
        print(f"No balance sheet section found in filing: {filing_link}")
        return None

    # Navigate to the table containing the balance sheet data
    balance_sheet_table = balance_sheet_section.find_next("table")

    # Extract the balance sheet data (example assumes 3 columns: Account, 2019 Value, 2018 Value)
    balance_sheet = []
    rows = balance_sheet_table.find_all("tr")[1:]  # Exclude header row
    for row in rows:
        cells = row.find_all("td")
        account = cells[0].text.strip()
        value_2019 = cells[1].text.strip()
        value_2018 = cells[2].text.strip()

        balance_sheet_row = {
            "account": account,
            "value_2019": value_2019,
            "value_2018": value_2018
        }
        balance_sheet.append(balance_sheet_row)

    return balance_sheet

# Example usage
cik = "0000320193"
filings = search_10k_filings(cik)

for filing in filings:
    balance_sheet = extract_balance_sheet(filing["link"])
    if balance_sheet:
        print(f"10-K Filing: {filing['title']}")
        for row in balance_sheet:
            print(f"- Account: {row['account']}")
            print(f"  2019 Value: {row['value_2019']}")
            print(f"  2018 Value: {row['value_2018']}")