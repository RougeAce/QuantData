from flask import Flask, render_template,request
from BackEnd import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('MainH.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        result = main.current_share_price(main.get_ticker(query))
        return render_template('MainH.html', Stock=(f"{query} current price per share is {result}"))
    else: # this block will execute for GET requests
        query = request.args.get('query')
        if query:
            result = main.current_share_price(main.get_ticker(query))
            return render_template('MainH.html', Stock=(f"{query} current price per share is {result}"))
    return render_template("error.html")


if __name__ == '__main__':
    app.run()
