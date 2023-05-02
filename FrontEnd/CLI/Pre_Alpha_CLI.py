from BackEnd import main

global x
x = 0

def get_user(Message):
    request = input(Message)
    return request

def proccese_data(inputs, x):
    possible_commands = command_options(x, print_statement=False)
    if x == 0:
        if inputs in possible_commands:
            if inputs == '--stock':
                stock_section()
    if x == 1:
        if inputs in possible_commands:
            if inputs == '--load':
                load_stock()



def command_options(x, print_statement=True):
    if print_statement:
        if x == 0:
            print("Current commands are --stock, --crypto, --economicdata, --quit")
        elif x == 1:
            print('Current commands are --load, --compare, --help, --quit')
    else:
        if x == 0:
            command = ['--stock', '--crypto', '--economicdata', '--quit']
            return command
        elif x == 1:
            command = ["--load", "--compare", "--help", "--quit"]
            return  command


'''This is the section where all of the stocks section commands go'''
def stock_section():
    global x
    print('Welcome to the stock section.')
    x = 1
    return 0

def load_stock():
    global x
    x = 1.1
    ticker = input("What is the ticker for the stock you would like to load")
    ticker = main.get_ticker(ticker)
    print(main.current_share_price(ticker))


print("Welcome to QuantCharts")
print("Currently we support stock, economic data, and crypto")

while True:
    command_options(x)
    command = get_user('Please enter a command: ')
    if command == "--quit":
        print("Recieived Exit Request: Breaking")
        break
    proccese_data(command, x)
