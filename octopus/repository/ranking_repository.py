from google.cloud import bigquery

client = bigquery.Client()
ranking_query = 'SELECT rank, country_full FROM `phoenix-cit.paul_2022.ranking` where rank_date=?'


def get_ranking(ranking_date):
    ranking = {}
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(None, "STRING", ranking_date)
        ])
    query_job = client.query(ranking_query, job_config=job_config)
    for row in query_job:
        ranking[row["country_full"]] = row["rank"]
    return ranking
