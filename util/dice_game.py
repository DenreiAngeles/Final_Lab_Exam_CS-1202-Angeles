import os
import time
import random
from util.user import User
from datetime import datetime

class DiceGame:
	def __init__(self, username):
		self.username = username
		self.score_folder = "scores"
		self.score_file = os.path.join(self.score_folder, "rankings.txt")
		self.create_score_folder()

	def create_score_folder(self):
		if not os.path.exists(self.score_folder):
			os.makedirs(self.score_folder)

	def load_scores(self):
		scores = []
		try:
			if os.path.exists(self.score_file):
				with open(self.score_file, "r") as file:
					for line in file:
						username, score, stage_score, date  = line.strip().split(",")
						scores.append((username,int(score),int(stage_score), date))
			return scores
		except FileNotFoundError:
			return None


	def save_scores(self, scores):
		with open(self.score_file, "w") as file:
			for username, score, stage_score, date in scores:
				file.write(f"{username},{score},{stage_score},{date}\n")

	def play_game(self):
		print(f"Starting game as {self.username}...")
		cpu_pts = 0
		user_pts = 0
		stage_wins = 0
		overall_pts = 0

		while True:
			for i in range(3):
				cpu_roll = random.randint(1, 6)
				user_roll = random.randint(1, 6)

				print(f"{self.username} rolled: {user_roll}")
				print(f"CPU rolled: {cpu_roll}")
				if cpu_roll < user_roll:
					user_pts += 1
					print(f"You win this round! {self.username}")
				if cpu_roll > user_roll:
					cpu_pts += 1
					print("CPU wins this round!")
				if cpu_roll == user_roll:
					print("It's a tie!")
				
			if cpu_pts < user_pts:
				user_pts += 3
				overall_pts += user_pts
				user_pts -= user_pts
				stage_wins += 1
				print(f"You won this stage! {self.username}")
				cont = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
				if cont == "1":
					continue
				elif cont == "0":
					final_score = overall_pts
					top_scores = self.load_scores()
					top_scores.append((self.username, final_score, stage_wins, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
					top_scores.sort(key=lambda x: x[1], reverse=True)
					top_scores = top_scores[:10]
					self.save_scores(top_scores)
					overall_pts -= overall_pts
					print(f"Game Over. You won {stage_wins} stages")
					stage_wins -= stage_wins
					break
				else:
					print("Invalid input. Please enter 1 for Yes or 0 for No")
					input("Press Enter to Continue...")
			if cpu_pts > user_pts:
				if stage_wins == 0:
					print(f"You lost this stage.")
					print("Game Over. You didn't win any stages")
					input("Press Enter to Continue...")
					break
				overall_pts += user_pts
				user_pts -= user_pts
				final_score = overall_pts
				top_scores = self.load_scores()
				top_scores.append((self.username, final_score, stage_wins, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
				top_scores.sort(key=lambda x: x[1], reverse=True)
				top_scores = top_scores[:10]
				self.save_scores(top_scores)
				overall_pts -= overall_pts
				print(f"You lost this stage.")
				print(f"Game Over. You won {stage_wins} stages")
				stage_wins -= stage_wins
				input("Press Enter to Continue...")
				break

	def show_top_scores(self):
		os.system('cls')
		print("Top Scores:")
		scores = self.load_scores()
		if not scores:
			print("No games played yet. Play a game to see top scores.")
		for index, (username, score, stage_score, date) in enumerate(scores, start = 1):
			print(f"{index}. {username}: Points - {score}, Wins - {stage_score} (Achieved on: {date})")
		input("Press Enter to Continue...")

	def logout(self):
		print(f"Goodbye, {self.username}")
		print("You logged out successfully")
		time.sleep(1)
		return True

	def menu(self):
		while True:
			os.system("cls")
			print(f"Welcome, {self.username}")
			print("Menu:")
			print("1. Start Game\n2. Show Top Scores\n3. Log Out")
			choice = input("Enter the number of your choice: ")
			if choice == "1":
				self.play_game()
			elif choice == "2":
				self.show_top_scores()
			elif choice == "3":
				if self.logout() == True:
					return
			else:
				print("Invalid choice. Please Try Again")
				time.sleep(1)
				continue