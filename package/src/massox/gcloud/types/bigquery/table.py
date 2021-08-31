from typing import Dict, Any

from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReference


class BigQueryTable:
    def __init__(self, dataset_reference: BigQueryDatasetReference, table_id: str):
        self._dataset_reference = dataset_reference
        self._table_id = table_id

    @property
    def dataset_reference(self):
        return self._dataset_reference

    @property
    def table_id(self):
        return self._table_id

    def to_api_repr(self) -> Dict[str, Any]:
        return self._dataset_reference.to_api_repr()


class BigQueryTableBuilder:
    def __init__(self):
        self._dataset_reference = None
        self._table_id = None

    def set_dataset_reference(self, dataset_reference: BigQueryDatasetReference):
        self._dataset_reference = dataset_reference

    def set_table_id(self, table_id: str):
        self._table_id = table_id

    def build(self) -> BigQueryTable:
        if self._dataset_reference is None:
            raise ValueError("Dataset reference is None")
        if self._table_id is None:
            raise ValueError("Table id is None")

        return BigQueryTable(
            dataset_reference=self._dataset_reference, table_id=self._table_id
        )
