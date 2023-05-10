import curses
import time
from BackEnd import main

def main_window(stdscr):
    # Clear the screen
    stdscr.clear()

    # Set up colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Set up the main window
    stdscr.addstr(0, 0, "Stock Price Monitor", curses.A_BOLD | curses.color_pair(1))
    stdscr.addstr(2, 0, "Enter a stock symbol: ")
    stdscr.refresh()

    # Get the stock symbol from the user
    symbol = stdscr.getstr(2, 21).decode()

    # Set up the price window
    price_win = curses.newwin(1, 20, 4, 0)
    price_win.addstr(0, 0, "Price: ")
    price_win.refresh()

    # Loop to update the price
    while True:
        price = main.current_share_price(main.get_ticker(symbol))
        price_win.addstr(0, 7, f"{price:.2f}")
        price_win.refresh()
        time.sleep(5)

# Set up curses and start the program
curses.wrapper(main_window)



