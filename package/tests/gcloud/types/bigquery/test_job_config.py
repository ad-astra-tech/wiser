import unittest


class BigQueryJobConfigTest(unittest.TestCase):
    def test_query_job_config_builder_no_write_disposition_raises_value_error(self):
        """
        GIVEN BigQueryQueryJobConfigBuilder
        WHEN  the write disposition is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.bigquery.job_config import (
            BigQueryQueryJobConfigBuilder,
        )
        from massox.gcloud.types.bigquery.table import BigQueryTableReferenceBuilder
        from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder

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
            .set_dataset_reference(dataset_reference=dataset_reference)
            .set_table_id(table_id=table_id)
            .build()
        )

        with self.assertRaises(ValueError):
            BigQueryQueryJobConfigBuilder().set_destination(
                destination=table_reference
            ).build()

    def test_query_job_config_builder_no_destination_raises_value_error(self):
        """
        GIVEN BigQueryQueryJobConfigBuilder
        WHEN  the write disposition is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.bigquery.job_config import (
            BigQueryQueryJobConfigBuilder,
        )
        from google.cloud.bigquery.job import WriteDisposition

        with self.assertRaises(ValueError):
            BigQueryQueryJobConfigBuilder().set_write_disposition(
                write_disposition=WriteDisposition.WRITE_TRUNCATE
            ).build()

    def test_query_job_config_builder_returns_query_job_config(self):
        """
        GIVEN BigQueryQueryJobConfigBuilder
        WHEN  the write disposition  and the destination are set
        THEN BigQueryJobConfig is returned
        """

        from google.cloud.bigquery.job import WriteDisposition
        from massox.gcloud.types.bigquery.job_config import (
            BigQueryQueryJobConfigBuilder,
        )
        from massox.gcloud.types.bigquery.table import BigQueryTableReferenceBuilder
        from massox.gcloud.types.bigquery.dataset import BigQueryDatasetReferenceBuilder
        from google.cloud.bigquery.job import QueryJobConfig

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
            .set_dataset_reference(dataset_reference=dataset_reference)
            .set_table_id(table_id=table_id)
            .build()
        )
        write_disposition = WriteDisposition.WRITE_TRUNCATE

        job_config = (
            BigQueryQueryJobConfigBuilder()
            .set_write_disposition(write_disposition=write_disposition)
            .set_destination(destination=table_reference)
            .build()
        )

        self.assertEqual(job_config.write_disposition, write_disposition)
        self.assertEqual(job_config.destination, table_reference)
        self.assertEqual(
            job_config.job_config.to_api_repr(),
            QueryJobConfig(
                destination=table_reference, write_disposition=write_disposition
            ).to_api_repr(),
        )
