import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid credentials")

while True:
    print("\n--- User Auth System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        register(uname, pwd)
    elif choice == "2":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        login(uname, pwd)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
