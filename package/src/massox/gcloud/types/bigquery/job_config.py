
from google.cloud.bigquery.job import QueryJobConfig

from massox.gcloud.types.bigquery.table import BigQueryTableReference
from massox.gcloud.types.bigquery.write_disposition import BigQueryWriteDisposition

class BigQueryQueryJobConfig:
    def __init__(self, destination: BigQueryTableReference, write_disposition: BigQueryWriteDisposition):
        self._destination = destination
        self._write_disposition = write_disposition

        self._job_config = QueryJobConfig(destination=destination, write_disposition=write_disposition)

    @property
    def destination(self) -> BigQueryTableReference:
        return self._destination

    @property
    def write_disposition(self) -> BigQueryWriteDisposition:
        return self._write_disposition

    @property
    def job_config(self) -> QueryJobConfig:
        return self._job_config




class BigQueryQueryJobConfigBuilder:
    def __init__(self):
        self._destination = None
        self._write_disposition = None

    def set_destination(self, destination: BigQueryTableReference) -> None:
        self._destination = destination

    def set_write_disposition(self, write_disposition: BigQueryWriteDisposition):
        self._write_disposition = write_disposition.value

    def build(self) -> BigQueryQueryJobConfig:
        if self._destination is None:
            raise ValueError("Destination is None")
        if self._write_disposition is None:
            raise ValueError("Write disposition is None")

        return BigQueryQueryJobConfig(
            destination=self._destination,
            write_disposition=self._write_disposition
        )