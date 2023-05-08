from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(url_for('search_results', query=query))
    else:
        query = request.args.get('query')
        return render_template('index.html', result=query)
    
@app.route('/search_results/<query>')
def query_results(query):
    return render_template('index.html', result=query)

if __name__ == '__main__':
    app.run()