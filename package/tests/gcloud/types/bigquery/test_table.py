import unittest


class BigQueryReferenceTableTest(unittest.TestCase):
    def test_table_reference_builder_no_table_id_raises_value_error(self):
        """
        GIVEN BigQueryTableReferenceBuilder
        WHEN  the the table id is not set
        THEN a value error is raised
        """

        from wiser.gcloud.types.bigquery.table import BigQueryTableReferenceBuilder
        from wiser.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

        dataset_id = "fake_dataset_id"
        project_id = "fake_project_id"

        dataset_reference = (
            BigQueryDatasetReferenceBuilder()
            .set_dataset_id(dataset_id=dataset_id)
            .set_project_id(project_id=project_id)
            .build()
        )
        with self.assertRaises(ValueError):
            BigQueryTableReferenceBuilder().set_dataset_reference(
                dataset_reference=dataset_reference
            ).build()

    def test_table_reference_builder_no_dataset_reference_raises_value_error(self):
        """
        GIVEN BigQueryTableReferenceBuilder
        WHEN  the dataset reference is not set
        THEN a value error is raised
        """

        from wiser.gcloud.types.bigquery.table import BigQueryTableReferenceBuilder

        table_id = "fake_table_id"

        with self.assertRaises(ValueError):
            BigQueryTableReferenceBuilder().set_table_id(table_id=table_id).build()

    def test_table_reference_builder_creates_table_reference(self):
        """
        GIVEN BigQueryTableReferenceBuilder
        WHEN  the dataset reference is not set
        THEN a value error is raised
        """

        from wiser.gcloud.types.bigquery.table import BigQueryTableReferenceBuilder
        from wiser.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder
        from google.cloud.bigquery.table import TableReference

        dataset_id = "fake_dataset_id"
        project_id = "fake_project_id"
        table_id = "fake_table_id"

        dataset_reference = (
            BigQueryDatasetReferenceBuilder()
            .set_dataset_id(dataset_id=dataset_id)
            .set_project_id(project_id=project_id)
            .build()
        )

        table_reference = (
            BigQueryTableReferenceBuilder()
            .set_table_id(table_id=table_id)
            .set_dataset_reference(dataset_reference=dataset_reference)
            .build()
        )

        self.assertEqual(
            table_reference.dataset_reference.to_api_repr(),
            dataset_reference.to_api_repr(),
        )
        self.assertEqual(table_reference.table_id, table_id)
        self.assertEqual(
            table_reference.reference.to_api_repr(),
            TableReference(
                dataset_ref=dataset_reference.dataset_reference,
                table_id=table_id,
            ).to_api_repr(),
        )
