import pytest

def test_dataset_reference_builder_no_project_id_raises_valueerror():
    """
    GIVEN BigQueryDatasetReferenceBuilder
    WHEN  the the project id is not set
    THEN a value error is raised
    """

    from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

    with pytest.raises(ValueError):
        BigQueryDatasetReferenceBuilder().set_dataset_id(
            dataset_id="fake_dataset_id"
        ).build()

def test_dataset_reference_builder_no_dataset_id_raises_valueerror():
    """
    GIVEN BigQueryDatasetReferenceBuilder
    WHEN  the the dataset id is not set
    THEN a value error is raised
    """

    from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

    with pytest.raises(ValueError):
        BigQueryDatasetReferenceBuilder().set_project_id(
            project_id="fake_project_id"
        ).build()

def test_dataset_reference_builder_return_dataset_reference():
    """
    GIVEN BigQueryDatasetReferenceBuilder
    WHEN  the the dataset id and the project id are set
    THEN a BigQueryDatasetReference object is returned
    """

    from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

    project_id = "fake_project_id"
    dataset_id = "fake_dataset_id"

    dataset_reference = BigQueryDatasetReferenceBuilder().set_project_id(
        project_id=project_id
    ).set_dataset_id(
        dataset_id=dataset_id
    ).build()

    assert dataset_reference.dataset_id == dataset_id
    assert dataset_reference.project_id == project_id
