from google.cloud import storage
from massox.connectors.gcloud.credentials import credentials


class StorageConnector:
    def __init__(self):
        self._client = storage.Client(credentials=credentials)

    def upload_from_string(
        self, data: bytes, bucket_name: str, destination_blob_name: str
    ):
        self._client.bucket(bucket_name=bucket_name).blob(
            blob_name=destination_blob_name
        ).upload_from_string(data=data)

    def upload_from_filename(
        self, source_file_name: str, bucket_name: str, destination_blob_name: str
    ):
        self._client.bucket(bucket_name=bucket_name).blob(
            blob_name=destination_blob_name
        ).upload_from_filename(filename=source_file_name)

    def download_as_string(self, bucket_name: str, source_blob_name: str):
        return (
            self._client.bucket(bucket_name=bucket_name)
            .blob(blob_name=source_blob_name)
            .download_as_bytes()
            .decode("utf-8")
        )

    def exists(self, bucket_name: str, source_blob_name: str):
        return (
            self._client.bucket(bucket_name=bucket_name)
            .blob(blob_name=source_blob_name)
            .exists()
        )

    def list_blobs(self, bucket_name: str, prefix: str = None, delimiter: str = None):
        return self._client.bucket(bucket_name=bucket_name).list_blobs(
            prefix=prefix, delimiter=delimiter
        )

    def copy(
        self,
        source_bucket_name: str,
        source_blob_name: str,
        dest_bucket_name: str,
        dest_blob_name: str,
    ):
        source_bucket = self._client.bucket(bucket_name=source_bucket_name)
        source_blob = source_bucket.blob(blob_name=source_blob_name)

        dest_bucket = self._client.bucket(bucket_name=dest_bucket_name)

        return source_bucket.copy_blob(
            blob=source_blob, destination_bucket=dest_bucket, new_name=dest_blob_name
        )

    def delete(self, bucket_name: str, blob_name: str):
        return (
            self._client.bucket(bucket_name=bucket_name)
            .blob(blob_name=blob_name)
            .delete()
        )


client = StorageConnector()
