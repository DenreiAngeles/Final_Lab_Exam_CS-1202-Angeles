from util.user_manager import UserManager
import time
import os

def main():
    while True:
        os.system('cls')
        um = UserManager()
        print("Welcome to Dice Roll Game!")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            um.register()
        elif choice == "2":
            um.login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please Try Again")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()