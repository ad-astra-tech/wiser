import json


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
            bucket_name=location.get_bucket(), source_blob_name=location.get_blob_name()
        )

        if location.filename.endswith(DataExtension.NUMPY.value):
            return np.frombuffer(data, dtype=np.float64)

        elif location.filename.endswith(DataExtension.JSON.value):
            return json.loads(data)
        else:
            NotImplementedError("File extension not managed for saving")
            return

    def save(self, obj, location: StorageLocation = None):
        data = None
        if location.filename.endswith(DataExtension.NUMPY.value):
            obj = obj.astype("float64")
            data = obj.tostring()

        elif location.filename.endswith(DataExtension.JSON.value):
            data = json.dumps(obj)
        else:
            NotImplementedError("File extension not managed for saving")
            return

        self._client.upload_from_string(
            data=data,
            bucket_name=location.get_bucket(),
            destination_blob_name=location.get_blob_name(),
        )

    def exists(self, location: StorageLocation = None):
        return self._client.exists(
            bucket_name=location.get_bucket(), source_blob_name=location.get_blob_name()
        )

    def get_list_content(self, location: StorageLocation = None) -> [StorageLocation]:
        blobs = self._client.list_blobs(
            bucket_name=location.get_bucket(), prefix=location.get_folders()
        )

        location_list = []
        for blob in blobs:
            if blob.name == location.get_folders():
                # blob is the folder, not a file
                continue
            blob_name = os.path.join(location.get_folders(), blob.name.split("/")[-1])
            base_location = (
                StorageLocationBuilder()
                .set_prefix(prefix=location.get_prefix())
                .set_bucket(bucket=location.get_bucket())
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
            source_bucket_name=source_location.get_bucket(),
            source_blob_name=source_location.get_blob_name(),
            dest_bucket_name=dest_location.get_bucket(),
            dest_blob_name=dest_location.get_blob_name(),
        )
        return self._client.delete(
            bucket_name=source_location.get_bucket(),
            blob_name=source_location.get_blob_name(),
        )
