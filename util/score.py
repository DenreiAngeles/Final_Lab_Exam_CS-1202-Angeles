from datetime import datetime

class Score:
	def __init__(self, username, game_id, points = 0, wins = 0):
		self.username = username
		self.game_id = game_id
		self.points = points
		self.wins = wins
	
	def update_score(self, points, wins):
		self.points += points
		self.wins += wins

	def reset_overall_score(self):
		self.points = 0
		self.wins = 0
	
	def to_record(self):
		self.game_id = datetime.now().strftime("%Y-%m-%d %I:%M %p")
		return self.username, self.points, self.wins, self.game_id