class Match:
    def __init__(self, country1, country2, country1_score, country2_score):
        self.country1 = country1
        self.country2 = country2
        self.country1_score = country1_score
        self.country2_score = country2_score

    def __str__(self):
        return f"""{self.country1} {self.country1_score} x {self.country2} {self.country2_score}"""
