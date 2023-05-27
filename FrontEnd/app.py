from flask import Flask
from GUI_RESOURCES.routes import index_route, search, search_stock, search_stock_price, search_stock_name
from GUI_RESOURCES.authentication import log, sign
from GUI_RESOURCES.signup import SU, request_signup_email, request_signup_username, request_code

app = Flask(__name__)

# Register routes
app.route('/')(index_route)
app.route('/search', methods=['GET'])(search)
app.route('/<query>')(search_stock)
app.route('/stock_price/<query>')(search_stock_price)
app.route('/stock_name/<query>')(search_stock_name)
app.route('/NAV/LOG')(log)
app.route('/SIGNIN')(sign)
app.route('/SIGNUP')(SU)
app.route('/SIGNUP/EMAIL', methods=['POST'])(request_signup_email)
app.route('/SIGNUP/USERNAME', methods=['POST'])(request_signup_username)
app.route('/requestsignup/requestauthentcation', methods=['POST'])(request_code)

if __name__ == '__main__':
    app.run()
