import requests
from bs4 import BeautifulSoup

def get_historical_cash_flows(cik):
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-K&count=5"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table_rows = soup.find_all('tr', class_='blueRow')

    cash_flows = []
    for row in table_rows:
        filing_date = row.find('td', class_='small').text.strip()
        document_link = row.find('td', class_='small').find('a')['href']
        cash_flows.append({'filing_date': filing_date, 'document_link': document_link})

    return cash_flows

cik = '0000320193'  # Apple's CIK

cash_flows = get_historical_cash_flows(cik)
if cash_flows:
    for filing in cash_flows:
        filing_date = filing['filing_date']
        document_link = filing['document_link']
        print(f"Filing Date: {filing_date}")
        print(f"Document Link: {document_link}")
        print("---")
else:
    print("No historical cash flow filings found.")



