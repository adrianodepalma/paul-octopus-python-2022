from octopus.utils import csv_utils


def get_matches_from_csv(gs_bucket_file):
    return csv_utils.read_csv_from_gs(gs_bucket_file)
