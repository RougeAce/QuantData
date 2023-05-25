import mysql.connector
import datetime

# Establish a connection to the MySQL server as root
def connect(database="QA", host="localhost", user="root", password=""):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QA"
    )
    return cnx

# Perform database operations...

def add_user_a(ID, mail, username, password):
    cnx = connect()
    cursor = cnx.cursor()
    query = "INSERT INTO USERS (ID, mail, username, password) VALUES (%s, %s, %s, %s)"
    values = (ID, mail, username, password)

    cursor.execute(query, values)


    cnx.commit()
    close(cnx)
    


def add_user_a(ID, mail, username, password):
    cnx = connect()
    cursor = cnx.cursor()
    query = "INSERT INTO USERS (ID, mail, username, password) VALUES (%s, %s, %s, %s)"
    values = (ID, mail, username, password)

    cursor.execute(query, values)
    
    cnx.commit()
    close(cnx)

    

def add_user_k(ID, key):
    cnx = connect()
    cursor = cnx.cursor()
    query = "INSERT INTO lockpick (id, lock_key) VALUES (%s, %s)"
    values = (ID, key)

    cursor.execute(query, values)

    cnx.commit()
    close(cnx)

def find_id(id):
    cnx = connect()
    cursor = cnx.cursor()
    query = "SELECT * FROM USERS WHERE ID = %s"
    cursor.execute(query, (id,))

    result = cursor.fetchone()

    close(cnx)
    return result

def find_username(username, password):
    cnx = connect()
    cursor = cnx.cursor()
    query = "SELECT * FROM USERS WHERE username = %s"
    cursor.execute(query, (username,))

    result = cursor.fetchone()
    if result is not None:
        stored_password = result[3]  # Assuming password is in the fourth column (index 3)
        if stored_password == password:
            # Passwords match
            close(cnx)
            return result

    # Username or password is incorrect
    close(cnx)
    return None


def find_usernameWP(username):
    cnx = connect()
    cursor = cnx.cursor()
    query = "SELECT * FROM USERS WHERE username = %s"
    cursor.execute(query, (username,))

    result = cursor.fetchone()

    close(cnx)
    return result

def find_user_id(username, password):
    cnx = connect()
    cursor = cnx.cursor()
    query = "SELECT ID FROM USERS WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    if result is not None:
        user_id = result[0]  # Assuming user ID is in the first column (index 0)
        close(cnx)
        return user_id

    # Username or password is incorrect
    close(cnx)
    return None


def close(cnx):
    cnx.close()
