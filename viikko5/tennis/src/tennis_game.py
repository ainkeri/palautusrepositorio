class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    WIN = 4

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.player_ones_score = 0
        self.player_twos_score = 0

        self.score = ""
        self.temporary_score = 0

    def won_point(self, player_name):
        if player_name == self.player_one:
            self.player_ones_score += 1
        elif player_name == self.player_two:
            self.player_twos_score += 1

    def same_score(self):
        if self.player_ones_score == self.LOVE:
            self.score = "Love-All"
        elif self.player_ones_score == self.FIFTEEN:
            self.score = "Fifteen-All"
        elif self.player_ones_score == self.THIRTY:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"
    
    def winning(self):
        minus_result = self.player_ones_score - self.player_twos_score

        if minus_result == 1:
            self.score = "Advantage Player 1"
        elif minus_result == -1:
            self.score = "Advantage Player 2"
        elif minus_result >= 2:
            self.score = "Win for Player 1"
        else:
            self.score = "Win for Player 2"

    def temp_score(self, player_score):
        if player_score == self.LOVE:
            self.score += "Love"
        elif player_score == self.FIFTEEN:
            self.score += "Fifteen"
        elif player_score == self.THIRTY:
            self.score += "Thirty"
        elif player_score == self.FORTY:
            self.score += "Forty"
          
    def get_score(self):
        self.score = ""

        if self.player_ones_score == self.player_twos_score:
            self.same_score()
        elif self.player_ones_score >= self.WIN or self.player_twos_score >= self.WIN:
            self.winning()
        else:
            self.temp_score(self.player_ones_score)
            self.score += "-"
            self.temp_score(self.player_twos_score)

        return self.score
