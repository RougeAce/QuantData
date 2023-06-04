from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class GreeksCalculator(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.option_contract = Contract()
        self.option_greeks = {}

    def nextValidId(self, orderId: int):
        # Request market data for the option contract
        self.reqMktData(1, self.option_contract, "", False, False, [])

    def tickOptionComputation(self, reqId: int, tickType: int, impliedVol: float, delta: float,
                              optPrice: float, pvDividend: float, gamma: float, vega: float,
                              theta: float, undPrice: float):
        self.option_greeks = {
            "Implied Volatility": impliedVol,
            "Delta": delta,
            "Option Price": optPrice,
            "Present Value of Dividends": pvDividend,
            "Gamma": gamma,
            "Vega": vega,
            "Theta": theta,
            "Underlying Price": undPrice
        }

    def calculate_option_greeks(self, symbol, secType, exchange, currency, expiry, strike, right):
        # Set up the option contract
        self.option_contract.symbol = symbol
        self.option_contract.secType = secType
        self.option_contract.exchange = exchange
        self.option_contract.currency = currency
        self.option_contract.lastTradeDateOrContractMonth = expiry
        self.option_contract.strike = strike
        self.option_contract.right = right

        # Connect to the TWS API
        self.connect("127.0.0.1", 7497, clientId=0)

        # Start the message loop
        self.run()


# Example usage
def main():
    # Create an instance of the GreeksCalculator
    greeks_calculator = GreeksCalculator()

    # Set the option contract details
    symbol = "AAPL"
    secType = "OPT"
    exchange = "SMART"
    currency = "USD"
    expiry = "20230616"
    strike = 150.0
    right = "C"

    # Calculate the option Greeks
    greeks_calculator.calculate_option_greeks(symbol, secType, exchange, currency, expiry, strike, right)

    # Wait for the option Greeks to be calculated
    while not greeks_calculator.option_greeks:
        pass

    # Display the calculated option Greeks
    for key, value in greeks_calculator.option_greeks.items():
        print(key + ": " + str(value))

    # Disconnect from the TWS API
    greeks_calculator.disconnect()


if __name__ == "__main__":
    main()
