from typing import List, Dict, Optional, Any

from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig


class BigQueryConnector:
    @staticmethod
    def query(
        query: str, job_config: QueryJobConfig = None
    ) -> Optional[bigquery.job.QueryJob]:
        if job_config is not None:
            return bigquery.Client().query(query, job_config=job_config)
        else:
            bigquery.Client().query(query)

    @staticmethod
    def insert(table: BigQueryTable, rows: List[Dict[str, Any]]):

        # Insert with checks
        errors = bigquery.Client().insert_rows_json(table.table_ref, rows)
        if errors:
            raise ValueError(
                "{} rows had errors and could not be inserted: {}".format(
                    len(errors), errors
                )
            )
        else:
            logger.info("Inserted.")
