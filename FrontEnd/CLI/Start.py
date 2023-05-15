import csv
import Stocks
import pandas as pd

global running
running = True
def start():
    print("Welcome to QuantData")
    print("This is a combination of APIS, Webscrappers, and repostiers that get data")
    print("What section would you like to enter")
    choice()

def quit(reason = "Quit request status = ACCEPTED"):
    print(reason)
    if reason == "Quit request status = ACCEPTED":
        print("NOTICE: If you did not submit a quit request, then there is an error")
        global running
        running = False

def choice():
    print("Commands are\n--login\n--signup\n--guest\n--quit")
    command = input("Enter your command: ")
    six = command[:6]
    seven = command[:7]
    eight = command[:8]

    if seven == "--login":
        log_in()
    elif eight == "--signup":
        sign_up()

    elif seven == "--guest":
        guest()

    elif six == "--quit":
        quit()
    else:
        print("Command could not be understood. Please input again")
        choice()


def log_in():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('accounts.csv')

    username_entered = input("Enter your username: ")
    password_entered = input(f"What is the password for {username_entered}? ")

    try:
        index = df.loc[df['Username'] == username_entered].index[0]
    except IndexError:
        print("Failed username or password")
        log_in()
    value = df.iloc[index, 1]
    if password_entered == value:
        print(f"Welcome {username_entered}")
    else:
        print("Failed username or password")
        log_in()




def sign_up():
    username = input("Enter the username you would like to use")
    password = input("The password you want to use")

    with open("accounts.csv", "a", newline="") as csvfile:
        # Create a writer object
        csvwriter = csv.writer(csvfile)

        # Write the username and password to the CSV file
        csvwriter.writerow([username, password])

    print("Account created successfully.")

def guest():
    print("Guest")
    section(Gues=True)


def section(Gues = False):
    commands = "The Possible Commands are\n--comodtites\n--crypto\n--econmic\n--forex\n--options\n--stocks"
    print(commands)
    command_entered = input("What command would you like to enter")
    seven = command_entered[:7]
    eight = command_entered[:8]
    nine = command_entered[:9]
    tweleve = command_entered[:12]
    if tweleve == "--comodtites":
        print(f"Welcome to {tweleve}")
    elif eight == "--crypto":
        print(f"Welcome to {eight}")
    elif nine == "--econmic":
        print(f"Welcome to {nine}")
    elif seven == "--forex":
        print(f"Weclome to {seven}")
    elif eight == "--options":
        print("Welcome to options")
    elif eight == "--stocks":
        print("Welcome to stocks")
        Stocks.stocks_start()
    else:
        print("command is invalid")
        section(Gues = Gues)




while running:
    start()
    print("Application must have malfuctioned")
    break











