from BackEnd import main

global stock


def get_commands(ticker, object = True, ALL = False):
    if object == True:
        keys = ticker.info.keys()
        if ALL == False:
            for i in keys:
                if i in ["marketCap", "regularMarketPreviousClose", "bid", "sharesShort", "bookValue", "priceToBook", "ebitda", "totalDebt", "totalCash", "freeCashflow"]:
                    print("--" + i)
                else:
                    continue
            print("--getALL")
            request_stock_data(ticker)
        else:
            for i in keys:
                print("--" + i)
                request_stock_data()


def stocks_start():
    for i in range(0, 100):
        print('\n')
    print("Stocks Section")
    commands = "Commands are\n--load\nquit"
    print(commands)
    command_entered = input("Enter a command")
    six = command_entered[:6]
    if six == "--load":
        symbol = command_entered.replace("--load", "")
        symbol = symbol.replace(" ", "")
        if symbol == "":
            symbol = input("What is the ticker of the stock you want to load")
        load_stock(symbol)

def load_stock(symbol):
    stock = main.get_ticker(symbol)
    print(main.current_share_price(stock))
    get_commands(stock)

def request_stock_data(ticker):
    command = input("What command would you like to enter:  ")
    command = command[2:]
    if command in ["marketCap", "regularMarketPreviousClose", "bid", "sharesShort", "bookValue", "priceToBook", "ebitda", "--totalDebt", "totalCash", "freeCashflow"]:
        print(f"The {command} is {main.get_something(ticker, command)}")
    elif command == "--more":
        get_commands(ticker, True, True)
    elif command == "quit":
        quit()
    else:
        print("Could not understand your command.")
        get_commands(ticker, True, False)
    keep = input("Would you like more information Y/N")
    keep = keep.upper()
    if keep == "Y":
        get_commands(ticker, True, False)
    if keep == "N":
        keep = input("Would you like to load a new stock Y/N")
        keep = keep.upper()
        if keep == "Y":
            load_stock()
        if keep == "N":
            quit()

def get_HIST_date(ticker, type, start_date, end_date, interval="1d", export=True, display = True):
    df = main.get_historical_data(ticker, [type], start_date, end_date, interval=interval, export=export)
    if display:
        print(df)







def quit():
    print("You have requested a quit so the application is done")
    running = False






