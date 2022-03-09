from msilib.schema import Error
from pathlib import Path
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

"""
generate_key()
"""

def load_key():
    return open("secret.key", "rb").read()

key = load_key()

fer = Fernet(key)

def loginAttempt() :
    with open("passwords.txt", "r") as f:
        masterPassword = f.readline()
        attempt = input("Please enter the master password: ")
    if fer.decrypt(masterPassword.encode()).decode() == attempt :
        print("Welcome")
    else : test()

def test() :
    while True :    
        mode = input("Failed login attempt, press a to try again or q to quit (a, q): ")    
        if mode == "a" :
            loginAttempt()
        elif mode == "q" :
            break


if Path('passwords.txt').is_file() :
    loginAttempt()
else : 
    masterPassword = input("Welcome to the password management program, please set the master password: ")
    with open("passwords.txt", "w") as f:
        f.write(fer.encrypt(masterPassword.encode()).decode())

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines()[1:]:
            data = line.rstrip()
            name, password = data.split("|")
            print("Name: " + name + " | Password: " + fer.decrypt(password.encode()).decode())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write("\n" + name + " | " + fer.encrypt(password.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? press q to quit ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print("Invalid selection")
        continue