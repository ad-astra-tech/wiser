from __future__ import annotations

from google.cloud.bigquery.job import QueryJobConfig
from google.cloud.bigquery.job import WriteDisposition

from wiser.gcloud.types.bigquery.table import BigQueryTableReference


class BigQueryQueryJobConfig:
    def __init__(
        self,
        destination: BigQueryTableReference,
        write_disposition: WriteDisposition,
    ):
        self._destination = destination
        self._write_disposition = write_disposition

        self._job_config = QueryJobConfig(
            destination=destination, write_disposition=write_disposition
        )

    @property
    def destination(self) -> BigQueryTableReference:
        return self._destination

    @property
    def write_disposition(self) -> WriteDisposition:
        return self._write_disposition

    @property
    def job_config(self) -> QueryJobConfig:
        return self._job_config


class BigQueryQueryJobConfigBuilder:
    def __init__(self):
        self._destination = None
        self._write_disposition = None

    def set_destination(
        self, destination: BigQueryTableReference
    ) -> BigQueryQueryJobConfigBuilder:
        self._destination = destination
        return self

    def set_write_disposition(
        self, write_disposition: WriteDisposition
    ) -> BigQueryQueryJobConfigBuilder:
        self._write_disposition = write_disposition
        return self

    def build(self) -> BigQueryQueryJobConfig:
        if self._destination is None:
            raise ValueError("Destination is None")
        if self._write_disposition is None:
            raise ValueError("Write disposition is None")

        return BigQueryQueryJobConfig(
            destination=self._destination, write_disposition=self._write_disposition
        )
