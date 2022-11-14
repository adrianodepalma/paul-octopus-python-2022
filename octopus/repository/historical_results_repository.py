from google.cloud import bigquery
from octopus.entity import historical_results
from octopus.utils.country_name_utils import get_country_name_in_results

client = bigquery.Client()
results_query = "SELECT avg(home_score),  avg(away_score) FROM `phoenix-cit.paul_2022.historical_results` " \
                "where home_team=? and away_team=?"


def get_historical_results(country1, country2):
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "STRING", get_country_name_in_results(country1)),
            bigquery.ScalarQueryParameter(None, "STRING", get_country_name_in_results(country2)),
        ])
    query_job = client.query(results_query, job_config=job_config)
    for row in query_job:
        if row[0] is None:
            return historical_results.HistoricalResults(country1, country2, 1, 1)
        else:
            return historical_results.HistoricalResults(country1, country2, row[0], row[1])
