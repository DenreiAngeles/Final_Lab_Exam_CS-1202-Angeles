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
		try:
			if os.path.exists(self.score_file):
				with open(self.score_file, "r") as file:
					for line in file:
						username, score, stage_score, date = line.strip().split(",")
						scores.append((username,int(score),int(stage_score), date))
			return scores
		except FileNotFoundError:
			return None

	def save_scores(self, scores):
		with open(self.score_file, "w") as file:
			for username, score, wins, game_id in scores:
				file.write(f"{username},{score},{wins},{game_id}\n")
	
	def continue_game(self):
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


	def play_game(self):
		os.system('cls')
		print(f"Starting game as {self.username}...")
		cpu_pts = 0
		user_pts = 0
		stage_wins = 0

		while True:
			for i in range(3):
				cpu_roll = random.randint(1, 6)
				user_roll = random.randint(1, 6)

				print(f"{self.username} rolled: {user_roll}")
				print(f"CPU rolled: {cpu_roll}")
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
					cpu_roll = random.randint(1, 6)
					user_roll = random.randint(1, 6)

					print(f"{self.username} rolled: {user_roll}")
					print(f"CPU rolled: {cpu_roll}")
					if cpu_roll < user_roll:
						user_pts += 1
						print(f"You win this round! {self.username}\n")
					if cpu_roll > user_roll:
						cpu_pts += 1
						print("CPU wins this round!\n")
					if cpu_roll == user_roll:
						print("It's a tie!\n")
		
			if cpu_pts < user_pts: #user wins
				user_pts += 3
				stage_wins += 1
				self.score.update_score(user_pts, stage_wins) #update overall score
				self.score.reset_score(user_pts) #reset game score
				print(f"\nYou won this stage! {self.username}\n")

				if self.continue_game(): 
					continue
				else:
					top_scores = self.load_scores() #list
					top_scores.append((self.score.to_record())) #add username, score, wins, date
					top_scores.sort(key=lambda x: x[1], reverse=True) #lambda x as criteria, reverse=True to reverse sort
					top_scores = top_scores[:10] #slice to only the first 10 index
					self.save_scores(top_scores) #save scores
					self.score.reset_overall_score() #reset overall score
					print(f"Game Over. You won {stage_wins} stages")
					break

			if cpu_pts > user_pts:
				if stage_wins == 0: #if no wins
					self.score.reset_score(user_pts)
					print(f"\nYou lost this stage.\n")
					print("Game Over. You didn't win any stages.")
					input("Press Enter to Continue...")
					break
				self.score.update_score(user_pts, stage_wins) #same kanina
				self.score.reset_score(user_pts)
				top_scores = self.load_scores()
				top_scores.append((self.score.to_record()))
				top_scores.sort(key=lambda x: x[1], reverse=True)
				top_scores = top_scores[:10]
				self.save_scores(top_scores)
				self.score.reset_overall_score()
				print(f"You lost this stage.")
				print(f"Game Over. You won {stage_wins} stages")
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