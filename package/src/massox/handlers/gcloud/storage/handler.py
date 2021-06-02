import json

from pathlib import Path

from massox.connectors.gcloud.storage.client import gcloud_storage_client
from massox.types.gcloud.storage.location import StorageLocation, StorageLocationBuilder
from massox.types.data.extensions import DataExtension


class GCloudStorageHandler:
    def __init__(self):
        self._name = "GCloudStorageHandler"
        self._client = gcloud_storage_client

    def __str__(self):
        return self._name

    def get(self, location: StorageLocation = None):
        data = self._client.download_as_string(
            bucket_name=location.bucket, source_blob_name=location.blob_name
        )

        if location.filename.endswith(DataExtension.NUMPY.value):
            return np.frombuffer(data, dtype=np.float64)

        elif location.filename.endswith(DataExtension.JSON.value):
            return json.loads(data)
        else:
            NotImplementedError("File extension not managed")
            return

    def save(self, obj, location: StorageLocation = None):
        data = None
        if location.filename.endswith(DataExtension.NUMPY.value):
            obj = obj.astype("float64")
            data = obj.tostring()
        elif location.filename.endswith(DataExtension.TEXT.value):
            data = obj
        elif location.filename.endswith(DataExtension.JSON.value):
            data = json.dumps(obj)
        else:
            NotImplementedError("File extension not managed")
            return

        self._client.upload_from_string(
            data=data,
            bucket_name=location.bucket,
            destination_blob_name=location.blob_name,
        )

    def exists(self, location: StorageLocation = None):
        return self._client.exists(
            bucket_name=location.bucket, source_blob_name=location.blob_name
        )

    def get_list_content(self, location: StorageLocation = None) -> [StorageLocation]:
        blobs = self._client.list_blobs(
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

    def move(
        self,
        source_location: StorageLocation = None,
        dest_location: StorageLocation = None,
    ):
        self._client.copy(
            source_bucket_name=source_location.bucket,
            source_blob_name=source_location.blob_name,
            dest_bucket_name=dest_location.bucket,
            dest_blob_name=dest_location.blob_name,
        )
        return self._client.delete(
            bucket_name=source_location.bucket,
            blob_name=source_location.blob_name,
        )
