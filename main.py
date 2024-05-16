from util.user import User
from util.dice_game import DiceGame
import time
import os

def main():
    while True:
        os.system('cls')
        user = User("","")
        print("Welcome to Dice Roll Game!")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            user.register()
        elif choice == "2":
            if user.login():
                login = DiceGame(user.username)
                login.menu()
        elif choice == "3":
            print("Exiting...")
            time.sleep(0.5)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please Try Again.")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()