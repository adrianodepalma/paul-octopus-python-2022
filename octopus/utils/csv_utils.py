from google.cloud import storage
import pandas as pd


def read_csv_from_gs(gs_bucket_file):
    client = storage.Client()
    data_frame = pd.read_csv(gs_bucket_file, encoding='utf-8')
    return data_frame
