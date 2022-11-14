from google.cloud import bigquery
from octopus.entity import historical_ratio

client = bigquery.Client()
historical_query = "SELECT games, wins, looses, draws FROM `phoenix-cit.paul_2022.historical_win-loose-draw_ratios` " \
                   "where country1=? and country2=?"


def get_historical_win_loose_draw_ratios(country1, country2):
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "STRING", country1),
            bigquery.ScalarQueryParameter(None, "STRING", country2),
        ])
    query_job = client.query(historical_query, job_config=job_config)
    for row in query_job:
        return historical_ratio.HistoricalRatio(country1, country2,
                                                row["games"], row["wins"], row["looses"], row["draws"])

    # return default value if there is no data (zero)
    return historical_ratio.HistoricalRatio(country1, country2, 0, 0, 0, 0)
