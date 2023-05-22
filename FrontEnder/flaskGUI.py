from flask import Flask, render_template, jsonify, redirect, request, url_for
import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Stock.html')


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search_query')
    print(f"Received query: {query}")
    return redirect(f"/{query}", code=302)

@app.route('/<query>')
def search_stock(query):
    try:
        ticker = main.get_ticker(symbol=query)
        stock_price = main.current_share_price(ticker)
        stock_name = main.ticker_name(ticker)
        return render_template('Stock.html', Corp_name=stock_name, stock_price=stock_price, ticker=query)
    except Exception as e:
        response = f"Could not find place {e}"
        return jsonify(response)


@app.route('/stock_price/<query>')
def search_stock_price(query):
    ticker = main.get_ticker(symbol=str(query))
    stock_price = main.current_share_price(ticker)
    return jsonify(stock_price=stock_price)

@app.route('/stock_name/<query>')
def search_stock_name(query):
    ticker = main.get_ticker(symbol=str(query))
    stock_name = main.ticker_name(ticker)
    return jsonify(stock_name=stock_name)




if __name__ == '__main__':
    app.run()
