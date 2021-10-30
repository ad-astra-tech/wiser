import unittest
from unittest.mock import patch

import google.cloud.storage

PROJECT = "PROJECT"
BUCKET_NAME = "BUCKET"
BLOB_NAME = "BLOB"


class StorageConnectorTest(unittest.TestCase):
    @staticmethod
    def _get_bucket(
        client: google.cloud.storage.Client, name: str
    ) -> google.cloud.storage.bucket.Bucket:
        """
        Returns a bucket

        @param client: a client to Google Cloud Storage
        @param name: the bucket name
        @return: a Bucket
        """
        from google.cloud.storage.bucket import Bucket

        return Bucket(client=client, name=name)

    @staticmethod
    def _get_blob(blob_name: str, bucket: google.cloud.storage.Bucket):
        """
        Returns a blob

        @param blob_name: the blob name
        @param bucket:  the bucket name
        @return:
        """
        from google.cloud.storage.blob import Blob

        return Blob(bucket=bucket, name=blob_name)

    @patch("google.cloud.storage.Blob.upload_from_string")
    def test_upload_from_string(self, upload_from_string_mock):
        """
        GIVEN   the StorageConnector
        WHEN    data in bytes format is passed to function `upload_from_string`
        THEN    None is returned
        """
        from massox.gcloud.connectors.storage import StorageConnector

        filename = "filename"
        data = bytes("hello".encode(encoding="utf-8"))
        upload_from_string_mock.return_value = None

        self.assertIsNone(
            StorageConnector.upload_from_string(
                data=data, bucket_name=BUCKET_NAME, destination_blob_name=filename
            )
        )

    @patch("google.cloud.storage.Blob.upload_from_filename")
    def test_upload_from_filename(self, upload_from_filename_mock):
        """
        GIVEN   the StorageConnector
        WHEN    data in bytes format is passed to function `upload_from_filename`
        THEN    None is returned
        """
        from massox.gcloud.connectors.storage import StorageConnector

        filename = "filename"

        upload_from_filename_mock.return_value = None

        self.assertIsNone(
            StorageConnector.upload_from_filename(
                source_file_name=filename,
                bucket_name=BUCKET_NAME,
                destination_blob_name=filename,
            )
        )

    @patch("google.cloud.storage.Client")
    @patch("google.cloud.storage.Bucket")
    def test_list_blobs(self, bucket_mock, client_mock):
        """
        GIVEN   the StorageConnector
        WHEN    list blobs invoked
        THEN    a list of blob names is returned
        """
        from massox.gcloud.connectors.storage import StorageConnector

        bucket = self._get_bucket(client=client_mock, name="BUCKET")
        blob_names = ["path/to/blob/1.ext", "path/to/blob/2.ext"]
        blobs_stubs = []
        for blob_name in blob_names:
            blobs_stubs.append(self._get_blob(blob_name=blob_name, bucket=bucket))

        bucket_mock.return_value.list_blobs.return_value = iter(blobs_stubs)

        self.assertEqual(blob_names, StorageConnector.list_blobs(bucket_name="BUCKET"))

    @patch("google.cloud.storage.Blob.exists")
    def test_exists_returns_True(self, exists_mock):
        """
        GIVEN   the StorageConnector
        WHEN    is checked whether exists a blob that exists
        THEN    True is returned
        """
        from massox.gcloud.connectors.storage import StorageConnector

        blob_name = "blob_that_exists"

        exists_mock.return_value = True

        self.assertIs(
            StorageConnector.exists(
                bucket_name=BUCKET_NAME, source_blob_name=blob_name
            ),
            True,
        )

    @patch("google.cloud.storage.Blob.exists")
    def test_exists_returns_False(self, exists_mock):
        """
        GIVEN   the StorageConnector
        WHEN    is checked whether exists a blob that exists
        THEN    False is returned
        """
        from massox.gcloud.connectors.storage import StorageConnector

        blob_name = "blob_that_does_not_exist"

        exists_mock.return_value = False

        self.assertIs(
            StorageConnector.exists(
                bucket_name=BUCKET_NAME, source_blob_name=blob_name
            ),
            False,
        )

    @patch("google.cloud.storage.Blob.download_as_bytes")
    def test_download_as_bytes(self, download_as_bytes_mock):
        """
        GIVEN   a bucket and a blob name
        WHEN    is used function `download_as_bytes`
        THEN    the content of data is retrieved
        """
        from massox.gcloud.connectors.storage import StorageConnector

        source_blob_name = "source_blob_name"
        data = bytes("This is the content of source_blob_name".encode(encoding="utf-8"))

        # Mocking functions
        download_as_bytes_mock.return_value = data

        self.assertEqual(
            StorageConnector.download_as_bytes(
                bucket_name=BUCKET_NAME, source_blob_name=source_blob_name
            ),
            data,
        )

    @patch("google.cloud.storage.Blob.download_as_bytes")
    def test_download_as_string(self, download_as_bytes_mock):
        """
        GIVEN   a bucket and a blob name
        WHEN    is used function `download_as_string`
        THEN    the content of data is retrieved
        """
        from massox.gcloud.connectors.storage import StorageConnector

        source_blob_name = "source_blob_name"
        data = bytes("This is the content of source_blob_name".encode(encoding="utf-8"))
        download_as_bytes_mock.return_value = data

        self.assertEqual(
            StorageConnector.download_as_string(
                bucket_name=BUCKET_NAME, source_blob_name=source_blob_name
            ),
            data.decode("utf-8"),
        )
