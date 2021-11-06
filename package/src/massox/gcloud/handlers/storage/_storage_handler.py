import json

from tempfile import NamedTemporaryFile

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

        if location.filename.endswith(FileExtension.NUMPY):
            data = StorageConnector.download_as_bytes(
                bucket_name=location.bucket, source_blob_name=location.blob_name
            )
            return np.frombuffer(data, dtype=np.float64)

        elif location.filename.endswith(FileExtension.JSON):
            data = StorageConnector.download_as_string(
                bucket_name=location.bucket, source_blob_name=location.blob_name
            )
            return json.loads(data)
        elif location.filename.endswith(FileExtension.TEXT):
            data = StorageConnector.download_as_string(
                bucket_name=location.bucket, source_blob_name=location.blob_name
            )
            return data
        else:
            NotImplementedError("File extension not managed")
            return

    @staticmethod
    def save(obj, location: StorageLocation = None):
        if location.filename.endswith(FileExtension.NUMPY):
            tmp_file = NamedTemporaryFile()
            np.save(file=tmp_file, arr=obj)
            StorageConnector.upload_from_filename(
                source_file_name=tmp_file.name,
                bucket_name=location.bucket,
                destination_blob_name=location.blob_name,
            )
            tmp_file.close()

        elif location.filename.endswith(FileExtension.TEXT):
            data = obj
            StorageConnector.upload_from_string(
                data=data,
                bucket_name=location.bucket,
                destination_blob_name=location.blob_name,
            )
        elif location.filename.endswith(FileExtension.JSON):
            data = json.dumps(obj)
            StorageConnector.upload_from_string(
                data=data,
                bucket_name=location.bucket,
                destination_blob_name=location.blob_name,
            )
        else:
            NotImplementedError("File extension not managed")
            return

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

        locations_list = []
        for blob_name in blobs:
            if blob_name == location.folders:
                # blob is the folder, not a file
                continue
            base_location = (
                StorageLocationBuilder()
                .set_bucket(bucket=location.bucket)
                .set_blob_name(blob_name=blob_name)
                .build()
            )
            locations_list.append(base_location)

        return locations_list

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
