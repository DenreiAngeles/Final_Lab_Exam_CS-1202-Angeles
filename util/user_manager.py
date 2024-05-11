import os
import time
from util.dice_game import DiceGame
from util.user import User

class UserManager:
    def __init__(self):
        self.user_folder = "user_data"
        self.user_file = os.path.join(self.user_folder, "users.txt")
        self.create_user_folder()
        
    def create_user_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_users(self):
        users = {}
        if os.path.exists(self.user_file):
            with open(self.user_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    users[username] = password
        return users

    def save_users(self, users):
        with open(self.user_file, "w") as file:
            for username, password in users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        users = self.load_users()
        return username in users

    def validate_password(self, username, password):
        users = self.load_users()
        return users.get(username) == password

    def register(self):
        while True:
            os.system('cls')
            print("Registration:\n")
            username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
            if not username:
                return
            if len(username) < 4:
                print("Username must be at least 4 characters long.")
                input("Press Enter to continue...")
                continue
            if self.validate_username(username):
                print("Username already exists.")
                input("Press Enter to continue...")
                continue
            
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if not password:
                return
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                input("Press Enter to continue...")
                continue

            users = self.load_users()
            users[username] = password
            self.save_users(users)
            print("Registration Successful.")
            time.sleep(1)
            return

    def login(self):
        while True:
            os.system('cls')
            print("Login:\n")
            username = input("Enter Username, or leave blank to cancel: ")
            if not username:
                return
            if not self.validate_username(username):
                print("Username does not exist.")
                input("Press Enter to Continue...")
                continue
            password = input("Enter Password, or leave blank to cancel: ")
            if not password:
                return
            if not self.validate_password(username, password):
                print("Incorrect password. Try again")
                input("Press Enter to Continue...")
                continue
            User(username, password)
            usermenu = DiceGame(username)
            usermenu.menu()
            
            return
