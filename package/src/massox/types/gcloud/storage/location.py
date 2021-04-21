from __future__ import annotations
import os


class StorageLocation:
    def __init__(
        self, prefix: str, bucket: str, blob_name: str, folders: str, filename: str
    ):
        self._prefix = prefix
        self._bucket = bucket
        self._blob_name = blob_name
        self._folders = folders
        self._filename = filename

    def get_prefix(self):
        return self._prefix

    def get_bucket(self):
        return self._bucket

    def get_folders(self):
        return self._folders

    def get_filename(self):
        return self._filename

    def get_blob_name(self):
        return self._blob_name

    def get_complete_path(self):
        return os.path.join(self._prefix, self._bucket, self._blob_name)


class StorageLocationBuilder:
    def __init__(self):
        self._prefix = "gs://"
        self._bucket = None
        self._blob_name = None

    def set_prefix(self, prefix: str) -> StorageLocationBuilder:
        self._prefix = prefix
        return self

    def set_bucket(self, bucket: str) -> StorageLocationBuilder:
        self._bucket = bucket
        return self

    def set_blob_name(self, blob_name: str) -> StorageLocationBuilder:
        self._blob_name = blob_name
        return self

    def build(self) -> StorageLocation:
        # Validating setting
        if self._bucket is None:
            raise ValueError("Bucket not set")

        if self._blob_name is None:
            raise ValueError("Blob name not set")

        # Getting filename from blob_name
        folders, filename = self._blob_name.split("/")

        return StorageLocation(
            prefix=self._prefix,
            bucket=self._bucket,
            folders=folders,
            blob_name=self._blob_name,
            filename=filename,
        )
