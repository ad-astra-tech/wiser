from typing import Dict

from google.cloud.bigquery.dataset import DatasetReference


class BigQueryDatasetReference:
    def __init__(self, dataset_id: str, project_id: str):
        self._dataset_id = dataset_id
        self._project_id = project_id

        self._dataset_reference = DatasetReference(project=project_id, dataset_id=dataset_id)

    @property
    def dataset_id(self) -> str:
        return self._dataset_id

    @property
    def project_id(self) -> str:
        return self._project_id

    def to_api_repr(self) -> Dict[str, str]:
        return self._dataset_reference.to_api_repr()


class BigQueryDatasetReferenceBuilder:
    def __init__(self):
        self._project_id = None
        self._dataset_id = None

    def set_project_id(self, project_id: str) -> None:
        self._project_id = project_id

    def set_dataset_id(self, dataset_id: str) -> None:
        self._dataset_id = dataset_id

    def build(self) -> BigQueryDatasetReference:
        if self._dataset_id is None:
            raise ValueError("Dataset id is None")
        if self._project_id is None:
            raise ValueError("Project id is None")

        return BigQueryDatasetReference(
            dataset_id=self._dataset_id, project_id=self._project_id
        )
