from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import string
import secrets
import os
import sys
from getpass import getpass

gray_blue = '\033[38;2;128;128;255m'
reset_color = '\033[0m'
void_space ="                                   "
platform = sys.platform

if platform == "linux" or platform == "linux2":

    clearterm = "clear"
else:
    clearterm = "cls"

def creating_folder():
    if os.path.exists(f"./auth/"):
        pass
        
    else:
        os.mkdir(f"./auth/")

def get_token():
    creating_folder()
    symbols = ['*', '%', '£'] # Can add more
    
    backend = default_backend()
    password = getpass("enter password: ")
    
    os.system(clearterm)
    try:
        f = open("auth/token.txt","rb")
        h = open("auth/salt.txt","rb")
        salt = h.read()
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(str(password),"ascii")))
        cipher_suite = Fernet(key)
        TOKEN_AUTH = str(cipher_suite.decrypt(f.read()))[2:-1]
        f.close()
        h.close()
        
    except:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
        auth_input =  getpass("token: ")
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password,"ascii")))
        cipher_suite = Fernet(key)
        f = open("auth/token.txt","wb")
        h = open("auth/salt.txt","wb")
        encoded_token = cipher_suite.encrypt(bytes(auth_input,"ascii"))
        f.write(encoded_token)
        TOKEN_AUTH = auth_input
        h.write(salt)
        f.close()
        h.close()
        os.system(clearterm)
    return TOKEN_AUTH   

def get_password():
    creating_folder()
    symbols = ['*', '%', '£'] # Can add more
    
    backend = default_backend()
    password = getpass("enter password: ")
    
    os.system(clearterm)
    try:
        f = open("auth/password.txt","rb")
        h = open("auth/salt_.txt","rb")
        salt = h.read()
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(str(password),"ascii")))
        cipher_suite = Fernet(key)
        PASSWORD_AUTH = str(cipher_suite.decrypt(f.read()))[2:-1]
        f.close()
        h.close()
        
    except:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
        auth_input = getpass(f"{void_space}{gray_blue}Password: ")
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password,"ascii")))
        cipher_suite = Fernet(key)
        f = open("auth/password.txt","wb")
        h = open("auth/salt_.txt","wb")
        encoded_token = cipher_suite.encrypt(bytes(auth_input,"ascii"))
        f.write(encoded_token)
        PASSWORD_AUTH = auth_input
        h.write(salt)
        f.close()
        h.close()
        os.system(clearterm)
    return PASSWORD_AUTH   