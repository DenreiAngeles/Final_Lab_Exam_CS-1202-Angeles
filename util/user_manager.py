import os

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
        return users[username] == password

    def register(self, username, password):
        users = self.load_users()
        users[username] = password
        self.save_users(users)

    def login(self, username, password):
        if not self.validate_username(username):
            return "Username does not exist."
        if not self.validate_password(username, password):
            return "Incorrect password. Try again"
        return "Login Successful."
