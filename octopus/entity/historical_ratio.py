class HistoricalRatio:
    def __init__(self, country1, country2, games, wins, losses, draws):
        self.country1 = country1
        self.country2 = country2
        self.games = games
        self.wins = wins
        self.losses = losses
        self.draws = draws

    def __str__(self):
        return f"""{self.country1} x {self.country2}
          Games: {self.games}
          {self.country1}:  {round(self.wins*100, 2)}% 
          {self.country2}:  {round(self.losses * 100, 2)}%
          Draws: {round(self.draws*100, 2)}%"""
