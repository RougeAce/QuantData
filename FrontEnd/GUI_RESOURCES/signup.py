from flask import render_template, request, jsonify

def SU():
    return render_template('SU.html')

def request_signup_email():
    data = request.get_json()
    email = data['email']

    # Need to add a system that checks if the user email already exists

    return "Code was received successfully"

def request_signup_username():
    data = request.get_json()
    username = data['username']

    # Need to add a system that checks if the username already exists

    return "Code was received successfully"

def request_code():
    data = request.get_json()
    email = str(data['email'])
    username = str(data['username'])
    password = str(data['password'])
    code = data['Code']

    start.check_code(UIC, code, password, email, username)

    return "Code authentication request received successfully", 200
