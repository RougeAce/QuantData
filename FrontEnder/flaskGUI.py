from flask import Flask, render_template, request, jsonify
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        print(f"the query is {query} from POST")
        return render_template('index.html', company_name=main.ticker_name(main.get_ticker(query.upper())))
    else:
        query = request.args.get('query')
        name = main.ticker_name(main.get_ticker(query.upper()))
        print(f"the company name is {name} from GET")
        return render_template('index.html', company_name=name)
    
@app.route('/search_results/<query>')
def query_results(query):
    print(f"the query is {query} from REDIRECT")
    return render_template('index.html', result=query, company_name=main.ticker_name(main.get_ticker(query.upper())))

# This is so an API or the computer itself can request data
@app.route('/api/<query>')
def get_stock_data(query):
    data = main.current_share_price(main.get_ticker(query.upper()))
    return str(data)

if __name__ == '__main__':
    app.run()