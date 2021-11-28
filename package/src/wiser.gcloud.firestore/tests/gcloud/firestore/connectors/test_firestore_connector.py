import unittest
from unittest.mock import patch

COLLECTION = "collection"
DOCUMENT = {"s": "S"}


class TestFirestoreConnector(unittest.TestCase):
    @patch("google.cloud.firestore_v1.document.DocumentReference.set")
    def test_add_returns_none(self, firestore_mock):
        """
        GIVEN the Firestore Connector
        WHEN valid parameters are passed to add function
        THEN None is returned
        """
        from wiser.gcloud.connectors.firestore.firestore_connector import (
            FirestoreConnector,
        )

        firestore_mock.return_value = None

        self.assertEqual(
            FirestoreConnector.add(
                collection_path=COLLECTION, document_id=None, data=DOCUMENT
            ),
            None,
        )

    @patch("google.cloud.firestore_v1.document.DocumentReference.update")
    def test_update_returns_none(self, firestore_mock):
        """
        GIVEN the Firestore Connector
        WHEN valid parameters are passed to add function
        THEN None is returned
        """
        from wiser.gcloud.connectors.firestore.firestore_connector import (
            FirestoreConnector,
        )

        firestore_mock.return_value = None

        self.assertEqual(
            FirestoreConnector.update(
                collection_path=COLLECTION, document_id="None", data=DOCUMENT
            ),
            None,
        )

    @patch("google.cloud.firestore_v1.query.Query.stream")
    def test_get_returns_list_dict(self, firestore_mock):
        """
        GIVEN the Firestore Connector
        WHEN valid parameters are passed
        THEN a list of dicts is returned
        """
        from wiser.gcloud.connectors.firestore.firestore_connector import (
            FirestoreConnector,
        )
        from google.cloud.firestore_v1.base_document import DocumentSnapshot

        stubs = [{"s": "S"} for _ in range(10)]
        document_snapshots = [
            DocumentSnapshot(
                data=data,
                reference=None,
                exists=True,
                read_time=None,
                create_time=None,
                update_time=None,
            )
            for data in stubs
        ]
        firestore_mock.return_value = document_snapshots

        self.assertEqual(
            FirestoreConnector.get(
                collection_name=COLLECTION, where_conditions=[("k", "==", "s")]
            ),
            stubs,
        )
