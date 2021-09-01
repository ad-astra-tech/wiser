

def test_storage_connector_init():
    """
    GIVEN the import massox.gcloud.connectors.storage import StorageConnector
    WHEN it's imported massox.gcloud.connectors.storage._storage_connector import StorageConnector
    THEN the types are the same
    """
    from massox.gcloud.connectors.storage import StorageConnector as InitStorageConnector
    from massox.gcloud.connectors.storage._storage_connector import StorageConnector as ScriptStorageConnector

    assert  type(InitStorageConnector) == type(ScriptStorageConnector)

