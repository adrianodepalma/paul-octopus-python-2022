class Match:

    def __init__(self, country1, country2, score1, score2):
        self.country1 = country1
        self.country2 = country2
        self.score1 = score1
        self.score2 = score2

    def __str__(self):
        return f"""{self.country1},{self.score1},{self.score2},{self.country2}"""
