class Player:
    def __init__(self, dict):
        self.player = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.player} team {self.team} goals {self.goals} assists {self.assists}"
