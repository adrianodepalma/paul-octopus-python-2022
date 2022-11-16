from google.cloud import storage
import pandas as pd

LINE_SEPARATOR = '\r\n'


def read_csv_from_gs(gs_bucket_file):
    client = storage.Client()
    data_frame = pd.read_csv(gs_bucket_file, encoding='utf-8')
    return data_frame


def get_csv_string_from_list(header, items):
    content = list()
    content.append(header)
    for item in items:
        content.append(LINE_SEPARATOR)
        content.append(str(item))
    return ''.join(content)
