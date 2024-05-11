class Score:
	def __init__(self, username, game_id, points = 0, wins = 0):
		self.username = username
		self.game_id = game_id
		self.points = points
		self.wins = wins
	
	def __str__(self):
		return f"Username: {self.username}, Points: {self.points}, Stages Won: {self.wins}"