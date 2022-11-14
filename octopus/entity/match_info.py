class MatchInfo:
    def __init__(self, country1, country2, ranking1, ranking2, historical_ratio, historical_results):
        self.country1 = country1
        self.country2 = country2
        self.ranking1 = ranking1
        self.ranking2 = ranking2
        self.historical_ratio = historical_ratio
        self.historical_results = historical_results

    def __str__(self):
        return f"""{self.historical_ratio}
          {self.country1}: {self.ranking1} (ranking)
          {self.country2}: {self.ranking2} (ranking)
          {self.historical_results}"""
