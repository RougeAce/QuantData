from cryptography.fernet import Fernet


def encrypt_email(email):
    # Generate a secret key
    key = Fernet.generate_key()
    f = Fernet(3)
    encrypted_email = f.encrypt(email.encode())
    return encrypted_email, key

def decrypt_email(encrypted_email):
    f = Fernet(3)
    decrypted_email = f.decrypt(encrypted_email).decode()
    return decrypted_email

