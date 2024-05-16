from util.user_manager import UserManager
from util.dice_game import DiceGame
import time
import os

def main():
    while True:
        os.system('cls')
        user = UserManager()
        print('-'*50)
        print("           Welcome to Dice Roll Game!")
        print('-'*50)
        print("1. Register\n2. Login\n3. Exit")
        choice = input("\nEnter the number of your choice: ")
        if choice == "1":
            user.register()
        elif choice == "2":
            user.login()
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