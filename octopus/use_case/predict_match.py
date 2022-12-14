from octopus.config import config
from octopus.entity import match

INDENTATION = '         '
MINIMUM_MATCHES = int(config.config['ALGORITHM']['MINIMUM_MATCHES'])
RANKING_SCORE_FACTOR = int(config.config['ALGORITHM']['RANKING_SCORE_FACTOR'])


def predict_match(match_info):
    print(match_info)

    if match_info.historical_ratio.games < MINIMUM_MATCHES:
        # if there are few matches between the two countries, it only uses the ranking to predict the result
        match_prediction = predict_match_from_ranking(match_info)
    else:
        match_prediction = predict_match_from_historical_results(match_info)

    print(INDENTATION, match_prediction, ' (prediction)')
    return match_prediction


def predict_match_from_ranking(match_info):
    # adds 1 goal for every RANKING_SCORE_FACTOR positions difference in the ranking
    ranking_difference = int(match_info.ranking1) - int(match_info.ranking2)
    winner_score = round(abs(ranking_difference) / RANKING_SCORE_FACTOR)

    if ranking_difference < 0:
        country1_score = winner_score
        country2_score = 0
    else:
        country1_score = 0
        country2_score = winner_score

    return match.Match(match_info.country1, match_info.country2, country1_score, country2_score)


def predict_match_from_historical_results(match_info):
    country1_score = match_info.historical_results.avg_home_score * match_info.historical_ratio.wins * 2
    country2_score = match_info.historical_results.avg_away_score * match_info.historical_ratio.losses * 2
    debug_match(match_info.country1, country1_score, match_info.country1, country2_score, ' (average * ratio)')

    return match.Match(match_info.country1, match_info.country2, round(country1_score), round(country2_score))


def debug_match(country1, score1, country2, score2, desc):
    print(INDENTATION, country1, ' ', round(score1, 2), ' x ', round(score2, 2),
          ' ', country2, desc)



