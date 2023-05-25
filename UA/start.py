from UA import Connect
from UA import EE
from UA import UAM
import hashlib
import random

global UIC



def create_code():
    code = []
    fcode = ''
    for i in range(6):
        i = random.randint(0, 9)
        code.append(i)
    for a in code:
        fcode += str(a)
        
    return fcode
    

def sign_in():
    def username(usernames):
        password = input("What is your password")
        password = hashlib.sha256(password.encode()).hexdigest()
        print(password)
        result = Connect.find_username(usernames, password)
        if result is not None:
            print("LogIn Succesful")
            global id
            id = Connect.find_user_id(usernames, password)
            print(id)
        else:
            print("LogIn Failed")
        return result
    
    
    EOU = input("What is your username")
    result = username(EOU)
    return result[0]
    
def create_new_id():
    id = []
    fid = ''
    for i in range(10):
        i = random.randint(0, 10)
        id.append(i)
    for a in id:
        fid += str(a)
        
    R = Connect.find_id(fid)
    
    if R is None:
        return fid
    else:
        return create_new_id()



def check_code(UIC, CODE, password, email, username):
    if UIC == CODE:
        password = hashlib.sha256(password.encode()).hexdigest()
        email, key = EE.encrypt_email(email)
        id = create_new_id()
        Connect.add_user_a(id, email, username, password)
        Connect.add_user_k(id, key)

    
def sign_up(username, email):
    result = Connect.find_usernameWP(username)
    
    if result is None:

        UIC = create_code()
        
        UAM.send_email("treydavidson2005@gmail.com", email, UIC)

        return UIC