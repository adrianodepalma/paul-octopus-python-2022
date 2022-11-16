# Scores will be calculated by checking the participant's predictions
# against the actual match scores, as stated below:
#
# Predicting that the match will have a winner:
# Exact match score: 25 points;
# Just the winner score: 18 points;
# Just the difference between the winner and the loser: 15 points;
# Just the loser score: 12 points;
# Just the winner team: 10 points;
#
# Predicting that the match result is a draw:
# Exact match score: 25 points;
# Just the match result (draw): 15 points;
# Any other score (not a draw): 4 points;

def calculate_points(match, prediction):
    diff_goals_prediction = int(prediction.score1) - int(prediction.score2)
    diff_goals_match = int(match.score1) - int(match.score2)
    is_draw = diff_goals_prediction == 0
    home_wins = diff_goals_prediction > 0
    away_wins = diff_goals_prediction < 0

    if (match.score1 == prediction.score1) and (match.score2 == prediction.score2):
        return 25

    if is_draw:
        if diff_goals_match == 0:
            return 15
        else:
            return 4

    if home_wins:
        if diff_goals_match <= 0:
            return 0
        elif prediction.score1 == match.score1:
            return 18
        elif diff_goals_prediction == diff_goals_match:
            return 15
        elif prediction.score2 == match.score2:
            return 12
        else:
            return 10

    if away_wins:
        if diff_goals_match >= 0:
            return 0
        elif prediction.score2 == match.score2:
            return 18
        elif diff_goals_prediction == diff_goals_match:
            return 15
        elif prediction.score1 == match.score1:
            return 12
        else:
            return 10

    return 0
