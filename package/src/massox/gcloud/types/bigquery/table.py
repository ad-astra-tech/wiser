from __future__ import annotations

from typing import Dict, Any

from google.cloud.bigquery.table import TableReference

from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReference


class BigQueryTableReference:
    def __init__(self, dataset_reference: BigQueryDatasetReference, table_id: str):
        self._dataset_reference = dataset_reference
        self._table_id = table_id
        self._table_reference = TableReference(
            dataset_ref=self._dataset_reference.dataset_reference,
            table_id=self._table_id,
        )

    @property
    def dataset_reference(self):
        return self._dataset_reference

    @property
    def table_id(self):
        return self._table_id

    @property
    def reference(self) -> TableReference:
        return self._table_reference

    def to_api_repr(self) -> Dict[str, Any]:
        return self._table_reference.to_api_repr()


class BigQueryTableReferenceBuilder:
    def __init__(self):
        self._dataset_reference = None
        self._table_id = None

    def set_dataset_reference(
        self, dataset_reference: BigQueryDatasetReference
    ) -> BigQueryTableReferenceBuilder:
        self._dataset_reference = dataset_reference
        return self

    def set_table_id(self, table_id: str) -> BigQueryTableReferenceBuilder:
        self._table_id = table_id
        return self

    def build(self) -> BigQueryTableReference:
        if self._dataset_reference is None:
            raise ValueError("Dataset reference is None")
        if self._table_id is None:
            raise ValueError("Table id is None")

        return BigQueryTableReference(
            dataset_reference=self._dataset_reference, table_id=self._table_id
        )
