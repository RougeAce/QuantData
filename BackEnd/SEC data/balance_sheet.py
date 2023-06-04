import requests
from BackEnd.Fred_Data import PASSWORD

API = str(PASSWORD.Alpha_API)
symbol = "AAPL"
year = "2020"

def get_data(symbol):
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API}"
    response = requests.get(url)
    data = response.json()
    return data


def get_total_revenue(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['totalRevenue']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"
def get_cost_of_revenue(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['costOfRevenue']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"
def get_gross_profit(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['grossProfit']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"
def get_rd_expenses(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['researchAndDevelopment']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"

def get_sga_expenses(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['sellingGeneralAndAdministrative']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"

def get_operating_income(symbol, year):
    try:
        Helllo = get_data(symbol)
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['operatingIncome']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"

def get_interest_and_tax_expenses(symbol, year):
    Helllo = get_data(symbol)
    try:
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['interestAndTaxExpenses']
                return result
        return "Error: Year not found"
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"

def get_net_income(symbol, year):
    Helllo = get_data(symbol)
    try:
        for i in Helllo['annualReports']:
            if i['fiscalDateEnding'][2] + i['fiscalDateEnding'][3] == str(year[2] + year[3]):
                result = i['netIncome']
                return result
    except KeyError:
        return "Error: Could not find the data you were looking for"
    except:
        return "Unknown Error occured"
    return "Error: Year not found"


# Example usage
symbol = 'AAPL'
year = '2020'

