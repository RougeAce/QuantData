import click
from BackEnd import main
import time
import threading


@click.group()
def cli():
    pass


@click.command()
@click.option("--name", prompt='Enter your name', help='The name of the user')
def hello(name):
    click.echo(f'HELLO {name}')



@click.command()
@click.option('--ticker', prompt='Enter the ticker you want to load', help='Enter ticker you want')
@click.option('--update', is_flag=True, help='Flag to continue updating stock price')
def stock(ticker, update):
    current_price = main.current_share_price(main.get_ticker(ticker))
    previous_close = main.previous_close_price(main.get_ticker(ticker))
    price_diff = current_price - previous_close

    if price_diff >= 0:
        color = '\033[32m'  # Green color
    else:
        color = '\033[31m'  # Red color

    click.echo(f'The current price of {ticker} is {color}${current_price}\033[0m', nl=False)

    if update:
        while True:
            time.sleep(1)
            current_price = main.current_share_price(main.get_ticker(ticker))
            previous_close = main.previous_close_price(main.get_ticker(ticker))
            price_diff = current_price - previous_close

            if price_diff >= 0:
                color = '\033[32m'  # Green color
            else:
                color = '\033[31m'  # Red color

            # Move the cursor to the beginning of the line and overwrite the previous price
            click.echo(f'\rThe current price of {ticker} is {color}${current_price}\033[0m', nl=False)


@click.command()
@click.option('--cryptopair', prompt='Enter the crypto pair you want to load', help='Enter ticker you want')
def crypto(pair):
    click.echo

cli.add_command(hello)
cli.add_command(stock)

if __name__ == '__main__':
    cli()




