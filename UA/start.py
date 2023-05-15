import Connect
import EE
import UAM
import hashlib
import random 



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
        

    
def sign_up():
    username = input("What username would you like to use")
    result = Connect.find_usernameWP(username)
    password = input("What password would you like to use")
    email = input("What is your email")
    
    if result is None:
    
        code = create_code()
        
        UAM.send_email("treydavidson2005@gmail.com", email, code)
        
        ucode = input("What code did you recieive in the email")
        
        if ucode == code:
            password = hashlib.sha256(password.encode()).hexdigest()
            email, key = EE.encrypt_email(email)
            id = create_new_id()
            Connect.add_user_a(id, email, username, password)
            Connect.add_user_k(id, key)
            
            
            
            
            

# Get the input
start = input("Would you like to sign in or sign up (SN/SU)")
start = start.upper()

# Check what it is
if start == "SI":
    sign_in()
if start == "SU":
    sign_up()