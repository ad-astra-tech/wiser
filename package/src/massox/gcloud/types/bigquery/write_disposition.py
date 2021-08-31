from enum import Enum

from google.cloud.bigquery.job import WriteDisposition


class BigQueryWriteDisposition(Enum):
    WRITE_TRUNCATE: WriteDisposition.WRITE_TRUNCATE
    WRITE_APPEND: WriteDisposition.WRITE_APPEND
    WRITE_EMPTY: WriteDisposition.WRITE_EMPTY