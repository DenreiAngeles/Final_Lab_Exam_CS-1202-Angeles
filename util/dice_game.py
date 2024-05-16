import os
import time
import random
from util.score import Score

class DiceGame:
	def __init__(self, username):
		self.username = username
		self.score_folder = "scores"
		self.score_file = os.path.join(self.score_folder, "rankings.txt")
		self.create_score_folder()
		self.score = Score(self.username,"")

	def create_score_folder(self):
		if not os.path.exists(self.score_folder):
			os.makedirs(self.score_folder)

	def load_scores(self):
		scores = []	
		if os.path.exists(self.score_file):
			with open(self.score_file, "r") as file:
				for line in file:
					username, score, stage_score, date = line.strip().split(",")
					scores.append((username,int(score),int(stage_score), date))
		return scores

	def save_scores(self, scores):
		with open(self.score_file, "w") as file:
			for username, score, wins, game_id in scores:
				file.write(f"{username},{score},{wins},{game_id}\n")

	def play_game(self):
		os.system('cls')
		print(f"Starting game as {self.username}...\n")
		stage_wins = 0
		stage = 1

		while True:
			cpu_pts = 0
			user_pts = 0
			def stage_display(stage):
				print('=============================')
				print(f'           STAGE {stage}         ')
				print('=============================')

			def continue_game():
				while True:
					cont = input("\nDo you want to continue to the next stage? (1 for Yes, 0 for No): ")
					if cont == "1":
						return True
					if cont == "0":
						return False
					else:
						print("Invalid input. Please enter 1 for Yes or 0 for No")
						input("Press Enter to Continue...")
						continue

			def score_saving():
				top_scores = self.load_scores()
				top_scores.append((self.score.to_record()))
				top_scores.sort(key=lambda x: x[1], reverse=True)
				top_scores = top_scores[:10]
				self.save_scores(top_scores)
				self.score.reset_overall_score()

			def roll_display(round):
				cpu_roll, user_roll = random.randint(1, 6), random.randint(1, 6)
				print(f"--Round {round}--")
				print(f"{self.username} rolled: {user_roll}")
				print(f"CPU rolled: {cpu_roll}")
				return cpu_roll, user_roll
			
			stage_display(stage)
			
			for round in range(3):
				cpu_roll, user_roll = roll_display(round+1)
				if cpu_roll < user_roll:
					user_pts += 1
					print(f"You win this round! {self.username}\n")
				if cpu_roll > user_roll:
					cpu_pts += 1
					print("CPU wins this round!\n")
				if cpu_roll == user_roll:
					print("It's a tie!\n")
				time.sleep(1)
			
			if cpu_pts == user_pts: #for best of three if game is tied
				while cpu_pts == user_pts:
					round += 1
					cpu_roll, user_roll = roll_display(round+1)
					if cpu_roll < user_roll:
						user_pts += 1
						print(f"You win this round! {self.username}\n")
					if cpu_roll > user_roll:
						cpu_pts += 1
						print("CPU wins this round!\n")
					if cpu_roll == user_roll:
						print("It's a tie!\n")
					time.sleep(1)
		
			if cpu_pts < user_pts: #user wins
				user_pts += 3
				stage_wins += 1
				self.score.update_score(user_pts, stage_wins) #update overall score
				print(f"{"="*50}\n	   You won this stage, {self.username}!\n{"="*50}")

				if continue_game():
					stage += 1 
					continue
				else:
					score_saving()
					if stage_wins < 2:
						print(f"{"="*50}\n     Game Over. You won {stage_wins} stage.\n{"="*50}")
					else:
						print(f"{"="*50}\n     Game Over. You won {stage_wins} stages.\n{"="*50}")
					break

			if cpu_pts > user_pts:
				if stage_wins == 0: #if no wins
					print(f"\nYou lost this stage.\n")
					print(f"{"="*50}\n	   Game Over. You didn't win any stages.\n{"="*50}")
					input("Press Enter to Continue...")
					break

				score_saving()
				self.score.update_score(user_pts, 0) #same kanina

				print(f"\nYou lost this stage.\n")
				if stage_wins < 2:
					print(f"{"="*50}\n     Game Over. You won {stage_wins} stage.\n{"="*50}")
				else:
					print(f"{"="*50}\n     Game Over. You won {stage_wins} stages.\n{"="*50}")
				input("Press Enter to Continue...")
				break

	def show_top_scores(self): #list top 10 scores
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
		print("You logged out successfully.")
		time.sleep(1)
		return True

	def menu(self):
		while True:
			os.system("cls")
			print('-'*20)
			print(f"   Welcome, {self.username}!")
			print('-'*20)
			print("\n=====MENU=====")
			print("1. Start Game\n2. Show Top Scores\n3. Log Out")
			choice = input("\nEnter the number of your choice: ")
			if choice == "1":
				self.play_game()
			elif choice == "2":
				self.show_top_scores()
			elif choice == "3":
				if self.logout():
					return
			else:
				print("Invalid choice. Please Try Again")
				time.sleep(1)
				continue