import unittest
from unittest.mock import patch

BUCKET = "bucket"
BLOB_NAME = "path/to/blob"


class StorageHandlerTest(unittest.TestCase):
    def test_get_with_location_no_blob_name_raises_value_error(self):
        """
        GIVEN   a location with no blob_name (i.e. a folder)
        WHEN    if invoked `get()` method
        THEN    value error is raised
        """
        from massox.gcloud.handlers.storage import StorageHandler
        from massox.gcloud.types.storage.location import StorageLocationBuilder

        location = StorageLocationBuilder().set_bucket(bucket=BUCKET).build()

        with self.assertRaises(ValueError):
            StorageHandler.get(location=location)


@patch("massox.gcloud.connectors.storage.StorageConnector.download_as_string")
class StorageHandlerTest(unittest.TestCase):
    def test_get_numpy_array(self, storage_connector_mock):
        """
        GIVEN   a valid location
        WHEN    the blob refers to a numpy array
        THEN    a numpy array is returned
        """
        from massox.gcloud.handlers.storage import StorageHandler
        from massox.gcloud.types.storage.location import StorageLocationBuilder
        import numpy as np

        location = (
            StorageLocationBuilder()
            .set_bucket(bucket=BUCKET)
            .set_blob_name(blob_name="path/to/file.npy")
            .build()
        )

        data = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
        bytessss = data.tobytes()
        datass = bytessss.decode(encoding="utf-8")
        storage_connector_mock.return_value = datass

        self.assertEqual(StorageHandler.get(location=location), data)
