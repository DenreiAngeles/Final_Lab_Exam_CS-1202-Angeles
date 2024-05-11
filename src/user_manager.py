import os
import time
from src.user import User

class UserManager:
    def __init__(self):
        username = None
        self.user_folder = "user_data"
        self.user_file = os.path.join(self.user_folder, f"{username}.txt")
        self.create_user_folder()
        
    def create_user_folder(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)

    def load_users(self, username):
        try:
            self.user_file = os.path.join(self.user_folder, f"{username}.txt")
            with open(self.user_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None

    def save_users(self, username, password):
        self.user_file = os.path.join(self.user_folder, f"{username}.txt")
        with open(self.user_file, "w") as file:
            file.write(password)
        
    def validate_username(self, username):
        if not os.path.exists(os.path.join(self.user_folder, f"{username}.txt")):
            return False
        return True

    def validate_password(self, username, password):
        stored_password = self.load_users(username)
        if stored_password.strip() == password:
            return True
        return False

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
            if os.path.exists(os.path.join(self.user_folder, f"{username}.txt")):
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
            self.save_users(username, password)
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
            if self.validate_username(username) == False:
                print("Username does not exist.")
                input("Press Enter to Continue...")
                continue
            password = input("Enter Password, or leave blank to cancel: ")
            if not password:
                return
            if self.validate_password(username, password) == False:
                print("Incorrect password. Try again")
                input("Press Enter to Continue...")
                continue
            game = User(username)
            game.user_menu()
