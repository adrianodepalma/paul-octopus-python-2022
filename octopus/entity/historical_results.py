class HistoricalResults:
    def __init__(self, country1, country2, avg_home_score, avg_away_score):
        self.country1 = country1
        self.country2 = country2
        self.avg_home_score = avg_home_score
        self.avg_away_score = avg_away_score

    def __str__(self):
        return f"""{self.country1} {round(self.avg_home_score, 2)} x {self.country2} {round(self.avg_away_score, 2)} (average)"""
