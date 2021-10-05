import unittest
from unittest.mock import patch

import google.cloud.storage

PROJECT = "PROJECT"
BUCKET_NAME = "BUCKET"
BLOB_NAME = "BLOB"


class StorageConnectorTest(unittest.TestCase):
    @staticmethod
    def _get_bucket(client: google.cloud.storage.Client, name: str) -> google.cloud.storage.bucket.Bucket:
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

    @patch("google.cloud.storage.Client")
    @patch("google.cloud.storage.Bucket")
    @patch("google.cloud.storage.Blob")
    def test_upload_from_string(self, BlobMock, BucketMock, ClientMock):
        """
        GIVEN   the StorageConnector
        WHEN    data in bytes format is passed to function `upload_from_string`
        THEN    None is returned
        """
        from massox.gcloud.connectors.storage._storage_connector import StorageConnector

        filename = "filename"
        data = bytes("hello".encode(encoding="utf-8"))

        self.assertIs(ClientMock, google.cloud.storage.Client)
        self.assertIs(BucketMock, google.cloud.storage.Bucket)
        self.assertIs(BlobMock, google.cloud.storage.Blob)

        self.assertIsNone(
            StorageConnector.upload_from_string(data=data, bucket_name=BUCKET_NAME, destination_blob_name=filename)
        )


    @patch("google.cloud.storage.Client")
    @patch("google.cloud.storage.bucket.Bucket")
    @patch("google.cloud.storage.blob.Blob")
    def test_download_as_string(self, BlobMock, BucketMock, ClientMock):
        """
        GIVEN   a bucket and a blob name
        WHEN    is used function `download_as_string`
        THEN    the content of data is retrieved
        """
        from massox.gcloud.connectors.storage._storage_connector import StorageConnector

        self.assertIs(ClientMock, google.cloud.storage.Client)
        self.assertIs(BucketMock, google.cloud.storage.bucket.Bucket)
        self.assertIs(BlobMock, google.cloud.storage.blob.Blob)

        source_blob_name = "source_blob_name"
        data = bytes("This is the content of source_blob_name".encode(encoding="utf-8"))

        # Mocking functions
        ClientMock.return_value.bucket.return_value = self._get_bucket(client=ClientMock, name=BUCKET_NAME)
        BucketMock.return_value.blob.return_value = self._get_blob(blob_name=source_blob_name, bucket=ClientMock.return_value.bucket)
        BlobMock.return_value.download_as_bytes.return_value = data

        self.assertEqual(
            StorageConnector.download_as_string(bucket_name=BUCKET_NAME, source_blob_name=source_blob_name), data.decode("utf-8")
        )