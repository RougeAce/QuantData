from flask import render_template

def log():
    return render_template('authentication.html')

def sign():
    return render_template('SN.html')
