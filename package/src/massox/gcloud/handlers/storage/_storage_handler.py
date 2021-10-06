import json

from pathlib import Path

import numpy as np

from massox.gcloud.connectors.storage import StorageConnector
from massox.gcloud.types.storage.location import StorageLocation, StorageLocationBuilder
from massox.gcloud.types.data.extensions import FileExtension


class StorageHandler:
    def __str__(self):
        return "Google Cloud Storage Handler"

    @staticmethod
    def get(location: StorageLocation = None):
        if location.blob_name is None:
            raise ValueError("No blob name given")

        data = StorageConnector.download_as_string(
            bucket_name=location.bucket, source_blob_name=location.blob_name
        )

        if location.filename.endswith(FileExtension.NUMPY):
            return np.frombuffer(data, dtype=np.float64)

        elif location.filename.endswith(FileExtension.JSON):
            return json.loads(data)
        else:
            NotImplementedError("File extension not managed")
            return

    @staticmethod
    def save(obj, location: StorageLocation = None):
        if location.filename.endswith(FileExtension.NUMPY):
            obj = obj.astype("float64")
            data = obj.tostring()
        elif location.filename.endswith(FileExtension.TEXT):
            data = obj
        elif location.filename.endswith(FileExtension.JSON):
            data = json.dumps(obj)
        else:
            NotImplementedError("File extension not managed")
            return

        StorageConnector.upload_from_string(
            data=data,
            bucket_name=location.bucket,
            destination_blob_name=location.blob_name,
        )

    @staticmethod
    def exists(location: StorageLocation = None):
        return StorageConnector.exists(
            bucket_name=location.bucket, source_blob_name=location.blob_name
        )

    @staticmethod
    def get_list_content(location: StorageLocation = None) -> [StorageLocation]:
        blobs = StorageConnector.list_blobs(
            bucket_name=location.bucket, prefix=location.folders
        )

        location_list = []
        for blob in blobs:
            if blob.name == location.folders:
                # blob is the folder, not a file
                continue
            blob_name = str(Path(location.folders).joinpath(blob.name.split("/")[-1]))
            base_location = (
                StorageLocationBuilder()
                .set_prefix(prefix=location.prefix)
                .set_bucket(bucket=location.bucket)
                .set_blob_name(blob_name=blob_name)
            )
            location_list.append(base_location)

        return location_list

    @staticmethod
    def move(
        source_location: StorageLocation = None,
        dest_location: StorageLocation = None,
    ):
        StorageConnector.copy(
            source_bucket_name=source_location.bucket,
            source_blob_name=source_location.blob_name,
            dest_bucket_name=dest_location.bucket,
            dest_blob_name=dest_location.blob_name,
        )
        return StorageConnector.delete(
            bucket_name=source_location.bucket,
            blob_name=source_location.blob_name,
        )
