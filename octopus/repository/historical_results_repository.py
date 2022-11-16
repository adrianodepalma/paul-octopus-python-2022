from google.cloud import bigquery
from octopus.entity import historical_results
from octopus.utils.country_name_utils import get_country_name_in_results
from octopus.entity import match

client = bigquery.Client()

results_query_by_countries = "SELECT avg(home_score),  avg(away_score) " \
                             "FROM `phoenix-cit.paul_2022.historical_results` " \
                             "where home_team=? and away_team=?"

results_query_by_year = "SELECT home_team, away_team, home_score, away_score, date " \
                        "FROM `phoenix-cit.paul_2022.historical_results` " \
                        "where tournament like 'FIFA World Cup' and EXTRACT(YEAR FROM date)=? order by date limit 48"


def get_historical_results(country1, country2):
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "STRING", get_country_name_in_results(country1)),
            bigquery.ScalarQueryParameter(None, "STRING", get_country_name_in_results(country2)),
        ])
    query_job = client.query(results_query_by_countries, job_config=job_config)
    for row in query_job:
        if row[0] is None:
            return historical_results.HistoricalResults(country1, country2, 1, 1)
        else:
            return historical_results.HistoricalResults(country1, country2, row[0], row[1])


def get_historical_results_from_world_cup(year):
    matches = []
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "INT64", int(year))
        ])
    query_job = client.query(results_query_by_year, job_config=job_config)
    for row in query_job:
        matches.append(match.Match(row[0], row[1], row[2], row[3]))

    return matches
