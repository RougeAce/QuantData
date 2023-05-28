from flask import render_template, request, jsonify
import UA

def SU():
    return render_template('SU.html')

def request_signup_email():
    data = request.get_json()
    pre_email = data['email']

    if UA.Connect.get_all_emails(pre_email) == True:
        return "Code was received successfully"
    else:
        return "Error"

def request_signup_username():
    data = request.get_json()
    pre_username = data['username']

    A = UA.Connect.find_usernameWP(pre_username)
    if A == None:
        global username
        username = pre_username
    else:
        return "Error1000"
    return "Username was received successfully"

def request_code():
    pass


def send_code(email, username, password):
    pass


def request_signup_password():
    data = request.get_json()
    global password
    password = data['password']

    return "Code was received successfully"




def request_code():
    data = request.get_json()
    email = str(data['email'])
    username = str(data['username'])
    password = str(data['password'])
    code = data['Code']

    UA.start.check_code(UIC, code, password, email, username)

    return "Code authentication request received successfully", 200
