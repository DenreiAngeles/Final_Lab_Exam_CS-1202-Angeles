from util.user_manager import UserManager
import os
import time

class User:
    def __init__(self, username, password, points = 0, stages_won = 0):
        self.username = username
        self.password = password
        self.points = points
        self.stages_won = stages_won
        self.um = UserManager()

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
            if self.um.validate_username(username):
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

            self.um.register(username, password)
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
            password = input("Enter Password, or leave blank to cancel: ")
            if not password:
                return
            login_status = self.um.login(username, password)
            if login_status == "Login Successful.":
                self.username = username
                print(login_status)
                time.sleep(1)
                return True
            else:
                print(login_status)
                input("Press Enter to Continue...")
                continue
		