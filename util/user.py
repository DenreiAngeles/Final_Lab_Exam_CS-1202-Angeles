class User:
    def __init__(self, username, password, points = 0, stages_won = 0):
        self.username = username
        self.password = password
        self.points = points
        self.stages_won = stages_won

    def __str__(self):
        return f"Username: {self.username}, Points: {self.points}, Stages Won: {self.stages_won}"
		