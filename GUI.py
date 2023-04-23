from flask import Flask, render_template,request
from BackEnd import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        result = main.current_share_price(main.get_ticker(query))
        return render_template('result.html', result=result)
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
