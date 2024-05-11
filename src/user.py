import os
import time

class User:
	def __init__(self, username):
		self.username = username
	
	def user_menu(self):
		os.system("cls")
		print(f"Welcome, {self.username}")
		print("Menu:")
		print("1. Start Game\n2. Show Top Scores\n3. Log Out")
		choice = input("Enter the number of your choice: ")
		if choice == "1":
			pass
		if choice == "2":
			pass
		if choice == "3":
			pass
		