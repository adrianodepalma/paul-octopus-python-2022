import functions_framework

from octopus.config.config import config
from octopus.entity.match_info import MatchInfo
from octopus.repository.historical_ratio_repository import get_historical_win_loose_draw_ratios
from octopus.repository.historical_results_repository import get_historical_results
from octopus.repository.matches_repository import get_matches_from_csv
from octopus.repository.ranking_repository import get_ranking
from octopus.use_case import predict_match
from octopus.utils.country_name_utils import get_country_name_in_ranking

ranking = {}


@functions_framework.http
def prediction(request):
    return "Paul the Octopus is alive!!!"


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


def predict():
    predictions = []

    global ranking
    ranking_date = config.get('ALGORITHM', 'RANKING_DATE')
    ranking = get_ranking(ranking_date)

    bucket_file_path = config.get('CLOUD_STORAGE', 'GS_BUCKET') + config.get('CLOUD_STORAGE', 'MATCHES_CSV_FILE')
    matches = get_matches_from_csv(bucket_file_path)

    for index, match in matches.iterrows():
        match_info = get_match_info(match['country1'], match['country2'])
        predictions.append(predict_match.predict_match(match_info))

    write_results(predictions)


def write_results(predictions):
    print(len(predictions))


def main():
    predict()


if __name__ == "__main__":
    main()