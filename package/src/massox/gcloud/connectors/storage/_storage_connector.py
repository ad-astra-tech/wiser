from google.cloud import storage
from massox.gcloud.connectors.credentials import credentials


class StorageConnector:
    @staticmethod
    def upload_from_string(data: bytes, bucket_name: str, destination_blob_name: str):
        storage.Client(credentials=credentials).bucket(bucket_name=bucket_name).blob(
            blob_name=destination_blob_name
        ).upload_from_string(data=data)

    @staticmethod
    def upload_from_filename(
        source_file_name: str, bucket_name: str, destination_blob_name: str
    ):
        storage.Client(credentials=credentials).bucket(bucket_name=bucket_name).blob(
            blob_name=destination_blob_name
        ).upload_from_filename(filename=source_file_name)

    @staticmethod
    def download_as_string(bucket_name: str, source_blob_name: str):
        return (
            storage.Client(credentials=credentials)
            .bucket(bucket_name=bucket_name)
            .blob(blob_name=source_blob_name)
            .download_as_bytes()
            .decode("utf-8")
        )

    @staticmethod
    def exists(bucket_name: str, source_blob_name: str):
        return (
            storage.Client(credentials=credentials)
            .bucket(bucket_name=bucket_name)
            .blob(blob_name=source_blob_name)
            .exists()
        )

    @staticmethod
    def list_blobs(bucket_name: str, prefix: str = None, delimiter: str = None):
        return (
            storage.Client(credentials=credentials)
            .bucket(bucket_name=bucket_name)
            .list_blobs(prefix=prefix, delimiter=delimiter)
        )

    @staticmethod
    def copy(
        source_bucket_name: str,
        source_blob_name: str,
        dest_bucket_name: str,
        dest_blob_name: str,
    ):
        client = storage.Client(credentials=credentials)
        source_bucket = client.bucket(bucket_name=source_bucket_name)
        source_blob = source_bucket.blob(blob_name=source_blob_name)

        dest_bucket = client.bucket(bucket_name=dest_bucket_name)

        return source_bucket.copy_blob(
            blob=source_blob, destination_bucket=dest_bucket, new_name=dest_blob_name
        )

    @staticmethod
    def delete(bucket_name: str, blob_name: str):
        return (
            storage.Client(credentials=credentials)
            .bucket(bucket_name=bucket_name)
            .blob(blob_name=blob_name)
            .delete()
        )
