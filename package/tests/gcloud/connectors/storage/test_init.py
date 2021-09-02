import unittest


class TestStorageInitModule(unittest.TestCase):
    def test_storage_connector_init(self):
        """
        GIVEN the import massox.gcloud.connectors.storage import StorageConnector
        WHEN it's imported massox.gcloud.connectors.storage._storage_connector import StorageConnector
        THEN the types are the same
        """
        from massox.gcloud.connectors.storage import (
            StorageConnector as InitStorageConnector,
        )
        from massox.gcloud.connectors.storage._storage_connector import (
            StorageConnector as ScriptStorageConnector,
        )

        self.assertEqual(type(InitStorageConnector), type(ScriptStorageConnector))
