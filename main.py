import functions_framework

from octopus.config.config import config
from octopus.entity import match
from octopus.entity.match_info import MatchInfo
from octopus.repository.historical_ratio_repository import get_historical_win_loose_draw_ratios
from octopus.repository.historical_results_repository import get_historical_results, \
    get_historical_results_from_world_cup
from octopus.repository.matches_repository import get_matches_from_csv
from octopus.repository.ranking_repository import get_ranking
from octopus.use_case import predict_match
from octopus.use_case.validate_points import calculate_points
from octopus.utils.country_name_utils import get_country_name_in_ranking
from octopus.utils.csv_utils import get_csv_string_from_list

import sys

ranking = {}

CSV_HEADER = 'home,home_score,away_score,away'
CURRENT_YEAR = 2022


@functions_framework.http
def ping(request):
    return "Paul the Octopus is alive!!!"


@functions_framework.http
def prediction(request):
    predictions = predict(CURRENT_YEAR)
    headers = {'Content-Type': 'text/csv', 'Content-Disposition': 'inline; filename="octopus_predictions.csv"'}
    text_csv = get_csv_string_from_list(CSV_HEADER, predictions)
    return text_csv, 200, headers


def get_ranking_position(country_name):
    country_name = get_country_name_in_ranking(country_name)
    return ranking[country_name]


def get_match_info(country1, country2):
    ranking1 = get_ranking_position(country1)
    ranking2 = get_ranking_position(country2)
    historical_ratio = get_historical_win_loose_draw_ratios(country1, country2)
    historical_results = get_historical_results(country1, country2)

    match_info = MatchInfo(country1, country2, ranking1, ranking2, historical_ratio, historical_results)

    return match_info


def get_matches(year):
    if int(year) == CURRENT_YEAR:
        matches = []
        bucket_file_path = config.get('CLOUD_STORAGE', 'GS_BUCKET') + config.get('CLOUD_STORAGE', 'MATCHES_CSV_FILE')
        csv_matches = get_matches_from_csv(bucket_file_path)
        for index, game in csv_matches.iterrows():
            matches.append(match.Match(game['country1'], game['country2'], '', ''))
        return matches
    else:
        return get_historical_results_from_world_cup(year)


def predict(year):
    predictions = []
    total_points = 0

    global ranking
    ranking_date = config.get('ALGORITHM', 'RANKING_DATE')
    ranking = get_ranking(ranking_date)

    matches = get_matches(year)

    for game in matches:
        match_info = get_match_info(game.country1, game.country2)
        match_prediction = predict_match.predict_match(match_info)
        predictions.append(match_prediction)
        if int(year) != CURRENT_YEAR:
            points = calculate_points(game, match_prediction)
            total_points += points
        print('         ', str(game), ' (official result)')
        print('         ', points, 'points')
        print('---------------------------------------------')

    if int(year) != CURRENT_YEAR:
        performance = total_points / (len(matches) * 25) * 100
        print('Performance: ', total_points, 'points, ', round(performance, 1), '%')

    return predictions


def main():
    if len(sys.argv) != 2:
        print('Please, inform the World Cup year as parameter. For example: ')
        print('python3 main.py 2022')
    else:
        year = sys.argv[1]
        print(get_csv_string_from_list(CSV_HEADER, predict(year)))


if __name__ == "__main__":
    main()
