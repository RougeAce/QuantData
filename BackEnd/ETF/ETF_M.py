import yfinance as yf
from datetime import datetime, timedelta

def calculate_price_change_removed_stocks():
    # Get the S&P 500 index data
    sp500 = yf.Ticker("^GSPC")

    # Get the index history
    index_history = sp500.history(period="max")

    # Filter the index history for stock removal dates since 2000
    removed_dates = index_history[index_history['Stock Splits'] != 0]

    for removed_date in removed_dates.index:
        stock_info = sp500.actions[sp500.actions.index == removed_date]
        removed_stocks = list(stock_info['Stock Splits'].keys())

        for stock in removed_stocks:
            # Get the stock data for three months after the removal date
            start_date = removed_date + timedelta(days=1)
            end_date = start_date + timedelta(days=90)
            stock_data = yf.download(stock, start=start_date, end=end_date)

            if len(stock_data) >= 2:
                start_price = stock_data['Close'].iloc[0]
                end_price = stock_data['Close'].iloc[-1]
                price_change = (end_price - start_price) / start_price * 100

                print("Stock:", stock)
                print("Removal Date:", removed_date.date())
                print("Start Price:", start_price)
                print("End Price:", end_price)
                print("Price Change (%):", price_change)
                print()

# Call the function
calculate_price_change_removed_stocks()


