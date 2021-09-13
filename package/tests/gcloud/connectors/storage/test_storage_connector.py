import unittest
from unittest.mock import patch

import google.cloud.storage
import mock
import requests

from six.moves import http_client

PROJECT = "PROJECT"
BUCKET_NAME = "BUCKET"
BLOB_NAME = "BLOB"


def _make_response(status=http_client.OK, content=b"", headers={}):
    response = requests.Response()
    response.status_code = status
    response._content = content
    response.headers = headers
    response.request = requests.Request()
    return response


class StorageConnectorTest(unittest.TestCase):
    @staticmethod
    def _make_credentials():
        import google.auth.credentials

        return mock.Mock(spec=google.auth.credentials.Credentials)

    @staticmethod
    def _get_client(credentials):
        from google.cloud.storage.client import Client

        return Client(credentials=credentials)

    @staticmethod
    def _get_bucket(client: google.cloud.storage.Client, name: str):
        from google.cloud.storage.bucket import Bucket

        return Bucket(client=client, name=name)

    @staticmethod
    def _get_blob(blob_name: str, bucket: google.cloud.storage.Bucket):
        from google.cloud.storage.blob import Blob

        return Blob(bucket=bucket, name=blob_name)

    def test(self):
        credentials = self._make_credentials()
        client = self._get_client(credentials=credentials)
        bucket = self._get_bucket(client, name=BUCKET_NAME)
        blob = self._get_blob(blob_name=BLOB_NAME, bucket=bucket)

    @patch("google.cloud.storage.Client")
    @patch("google.cloud.storage.Bucket")
    @patch("google.cloud.storage.Blob")
    def test_upload_from_string(self, BlobMock, BucketMock, ClientMock):
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
    @patch("google.cloud.storage.Bucket")
    @patch("google.cloud.storage.Blob")
    def test_download_as_string(self, BlobMock, BucketMock, ClientMock):
        from massox.gcloud.connectors.storage._storage_connector import StorageConnector

        self.assertIs(ClientMock, google.cloud.storage.Client)
        self.assertIs(BucketMock, google.cloud.storage.Bucket)
        self.assertIs(BlobMock, google.cloud.storage.Blob)

        source_blob_name = "source_blob_name"
        data = bytes("This is the content of source_blob_name".encode(encoding="utf-8"))

        BlobMock.return_value = data
        print(BlobMock.return_value)
        print(StorageConnector.download_as_string(bucket_name=BUCKET_NAME, source_blob_name=source_blob_name))
        self.assertEqual(
            StorageConnector.download_as_string(bucket_name=BUCKET_NAME, source_blob_name=source_blob_name), data
        )