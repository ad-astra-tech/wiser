from __future__ import annotations

from pathlib import Path


class StorageLocation:
    def __init__(self, prefix: str, bucket: str, blob_name: str, folders: str, filename: str):
        self._prefix = prefix
        self._bucket = bucket
        self._blob_name = blob_name
        self._folders = folders
        self._filename = filename

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def folders(self) -> str:
        return self._folders

    @property
    def blob_name(self) -> str:
        return self._blob_name

    @property
    def bucket(self) -> str:
        return self._bucket

    @property
    def prefix(self) -> str:
        return self._prefix

    def complete_path(self):
        return str(self.prefix) + str(Path(self.bucket).joinpath(self.blob_name))


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
        filename = None
        folders = self._blob_name
        if "." in Path(self._blob_name).name:
            values = self._blob_name.split("/")
            filename = values[-1]
            folders = "/".join(values[:-1])

        return StorageLocation(
            prefix=self._prefix,
            bucket=self._bucket,
            folders=folders,
            blob_name=self._blob_name,
            filename=filename,
        )
