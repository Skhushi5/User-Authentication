from database import users
from hashlib import sha256

logged_in = False

def print_menu():
    print("""What do you want to do?
1. Register
2. Login
3. Logout
4. Delete Account
5. Exit
""")

def register():
    global logged_in, users
    username = input("Enter your username: ")
    while username in users:
        print("Username already exists.")
        username = input("Enter your username or enter exit to leave: ")
        if username == "exit":
            return
    password = input("Enter your password: ")
    confirm_password = input("Enter your password again to confirm: ")
    while password != confirm_password:
        print("Both Passwords don't match.")
        password = input("Enter your password or enter exit to leave: ")
        if password == "exit":
            return
        confirm_password = input("Enter your password again to confirm: ")
    users[username] = sha256(password.encode()).hexdigest()
    logged_in = username

def login():
    global logged_in
    if logged_in != False:
        print(f"You are already logged in as {logged_in}. Logout before logging in again.")
        return
    username = input("Enter your username: ")
    while username not in users:
        print("This user doesn't exist.")
        username = input("Enter your username or enter exit to leave: ")
        if username == "exit":
            return
    password = input("Enter your password: ")
    while sha256(password.encode()).hexdigest() != users[username]:
        print("Incorrect Password.")
        password = input("Enter your password or enter exit to leave or change username: ")
        if password == "exit":
            return
    logged_in = username

def logout():
    global logged_in
    if logged_in == False:
        print("You are not logged in.")
        return
    logged_in = False
    print("Logged out successfully.")

def delete_account():
    global logged_in, users
    if logged_in == False:
        print("You need to be logged in to delete your account.")
        return
    password = input("Enter your password to confirm deleting your account: ")
    while sha256(password.encode()).hexdigest() != users[logged_in]:
        print("Incorrect Password.")
        password = input("Enter your password to confirm deleting your account or enter exit to leave: ")
        if password == "exit":
            return
    users.pop(logged_in)
    logged_in = False


def save_database():
    database = open('database.py','w')
    database.write(f'users = {users}')
    database.close()
    print("Database Updated")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            print()
            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                logout()
            elif choice == 4:
                delete_account()
            elif choice == 5:
                break
            else:
                print("Invalid Choice")
        except:
            print("Invalid Choice")
        finally:
            print()
    save_database()

if __name__ == '__main__':
    main()