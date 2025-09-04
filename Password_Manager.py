from os import close

from cryptography.fernet import Fernet

#In the first run, you need to remove the comment in the write_key() function to generate a key. After that, you need to comment it out; otherwise, it will generate multiple keys.
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#master_pwd = input("Enter the Master Password: ")
key = load_key()
fer = Fernet(key)

def view():
    with open('Passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data: #ensure correct format
                user, passw = data.split("|", 1)
                print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())
            else:
                print("Skipping invalid line:", data)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('Passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you to add a new password or view existing ones (view, add), press q to quit.").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid node.")
        continue