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
        from massox.gcloud.services.storage import Storage
        from massox.gcloud.types.storage.location import StorageLocationBuilder

        location = StorageLocationBuilder().set_bucket(bucket=BUCKET).build()

        with self.assertRaises(ValueError):
            Storage.get(location=location)


@patch("massox.gcloud.connectors.storage.StorageConnector.download_as_string")
class StorageHandlerTest(unittest.TestCase):
    def test_get_stromg(self, storage_connector_mock):
        """
        GIVEN   a valid location
        WHEN    the blob refers to a string
        THEN    the expected string is returned
        """
        from massox.gcloud.services.storage import Storage
        from massox.gcloud.types.storage.location import StorageLocationBuilder
        import numpy as np

        location = (
            StorageLocationBuilder()
            .set_bucket(bucket=BUCKET)
            .set_blob_name(blob_name="path/to/text.txt")
            .build()
        )

        data = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
        storage_connector_mock.return_value = data

        self.assertEqual(Storage.get(location=location), data)
