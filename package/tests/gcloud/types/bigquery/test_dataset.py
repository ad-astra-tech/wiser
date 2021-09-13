import unittest


class BigQueryDatasetReferenceTest(unittest.TestCase):
    def test_dataset_reference_builder_no_project_id_raises_valueerror(self):
        """
        GIVEN BigQueryDatasetReferenceBuilder
        WHEN  the the project id is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

        with self.assertRaises(ValueError):
            BigQueryDatasetReferenceBuilder().set_dataset_id(
                dataset_id="fake_dataset_id"
            ).build()

    def test_dataset_reference_builder_no_dataset_id_raises_valueerror(self):
        """
        GIVEN BigQueryDatasetReferenceBuilder
        WHEN  the the dataset id is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

        with self.assertRaises(ValueError):
            BigQueryDatasetReferenceBuilder().set_project_id(
                project_id="fake_project_id"
            ).build()

    def test_dataset_reference_builder_return_dataset_reference(self):
        """
        GIVEN BigQueryDatasetReferenceBuilder
        WHEN  the the dataset id and the project id are set
        THEN a BigQueryDatasetReference object is returned
        """

        from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder
        from google.cloud.bigquery.dataset import DatasetReference

        project_id = "fake_project_id"
        dataset_id = "fake_dataset_id"

        dataset_reference = (
            BigQueryDatasetReferenceBuilder()
            .set_project_id(project_id=project_id)
            .set_dataset_id(dataset_id=dataset_id)
            .build()
        )

        self.assertEqual(dataset_reference.dataset_id, dataset_id)
        self.assertEqual(dataset_reference.project_id, project_id)
        self.assertEqual(
            dataset_reference.to_api_repr(),
            DatasetReference(project=project_id, dataset_id=dataset_id).to_api_repr(),
        )
