class Player:
    def __init__(self, dict):
        self.player = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.player:20}{self.team} {self.goals} + {self.assists} = {self.goals+self.assists}"
