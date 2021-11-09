from typing import List, Dict, Optional, Any

from google.cloud import bigquery

from wiser.gcloud.types.bigquery.table import BigQueryTableReference
from wiser.gcloud.types.bigquery.job_config import BigQueryQueryJobConfig


class BigQueryConnector:
    @staticmethod
    def query(
        query: str, job_config: BigQueryQueryJobConfig = None
    ) -> Optional[bigquery.job.QueryJob]:
        if job_config is not None:
            return bigquery.Client().query(query, job_config=job_config.job_config)
        else:
            bigquery.Client().query(query)

    @staticmethod
    def insert(table: BigQueryTableReference, rows: List[Dict[str, Any]]):

        # Insert with checks
        errors = bigquery.Client().insert_rows_json(table.reference, rows)
        if errors:
            raise ValueError(
                "{} rows had errors and could not be inserted: {}".format(
                    len(errors), errors
                )
            )
