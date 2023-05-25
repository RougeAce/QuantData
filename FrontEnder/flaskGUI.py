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


#  Authentication Section
@app.route('/NAV/LOG')
def log():
    return render_template('authentication.html')

# Sign In section
@app.route('/SIGNIN')
def sign():
    return render_template('SN.html')

# Sign Up section

@app.route('/SIGNUP')
def SU():
    return render_template('SU.html')


@app.route('/requestsignup', methods=['POST'])
def request_signup():
    data = request.get_json()
    email = data['email']
    username = data['username']
    password = data['password']

    # Process the data as needed

    return f'we received email as {email}' \
           f'passowrd as {password}' \
           f'username as {username}'









if __name__ == '__main__':
    app.run()
