import unittest
from unittest.mock import patch


class TestFirestoreService(unittest.TestCase):
    def test_add_wrong_types_raises_value_error(self):
        """
        GIVEN the FirestoreService
        WHEN are passed illegal parameters to add function
        THEN value errors are raised
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreDocumentBuilder,
            FirestoreCollectionBuilder,
        )

        collection_name = "my_collection"
        data = {"key": "Value"}
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        document = FirestoreDocumentBuilder().set_data(data=data).build()

        with self.assertRaises(ValueError):
            Firestore.add(collection=collection_name, document=document)

        with self.assertRaises(ValueError):
            Firestore.add(collection=collection, document=data)

        with self.assertRaises(ValueError):
            Firestore.add(collection=collection_name, document=data)

    @patch(
        "wiser.gcloud.connectors.firestore.firestore_connector.FirestoreConnector.add"
    )
    def test_firestore_add_returns_none(self, firestore_connector_mock):
        """
        GIVEN the Firestore service
        WHEN add functions parameters are valid
        THEN none is returned
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreDocumentBuilder,
            FirestoreCollectionBuilder,
        )

        collection_name = "my_collection"
        data = {"key": "Value"}
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        document = FirestoreDocumentBuilder().set_data(data=data).build()

        firestore_connector_mock.return_value = None

        self.assertEqual(Firestore.add(collection=collection, document=document), None)

    def test_firestore_update_invalid_parameters_raises_value_error(self):
        """
        GIVEN the FirestoreService
        WHEN are passed illegal parameters to update function
        THEN value errors are raised
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreDocumentBuilder,
            FirestoreCollectionBuilder,
        )

        collection_name = "my_collection"
        data = {"key": "Value"}
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        document = FirestoreDocumentBuilder().set_data(data=data).build()

        with self.assertRaises(ValueError):
            Firestore.update(collection=collection_name, document=document)

        with self.assertRaises(ValueError):
            Firestore.update(collection=collection, document=data)

        with self.assertRaises(ValueError):
            Firestore.update(collection=collection_name, document=data)

    def test_firestore_update_raises_value_error(self):
        """
        GIVEN the Firestore service
        WHEN no document id is provided to FirestoreDocument
        THEN value error is raised
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreDocumentBuilder,
            FirestoreCollectionBuilder,
        )

        collection_name = "my_collection"
        data = {"key": "Value"}
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        document = FirestoreDocumentBuilder().set_data(data=data).build()
        with self.assertRaises(ValueError):
            Firestore.update(collection=collection, document=document)

    @patch(
        "wiser.gcloud.connectors.firestore.firestore_connector.FirestoreConnector.update"
    )
    def test_firestore_update_returns_none(self, firestore_connector_mock):
        """
        GIVEN the Firestore service
        WHEN add functions parameters are valid
        THEN none is returned
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreDocumentBuilder,
            FirestoreCollectionBuilder,
        )

        collection_name = "my_collection"
        data = {"key": "Value"}
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        document = (
            FirestoreDocumentBuilder().set_id(id="1234").set_data(data=data).build()
        )

        firestore_connector_mock.return_value = None

        self.assertEqual(
            Firestore.update(collection=collection, document=document), None
        )

    def test_firestore_get_invalid_parameters_raises_value_error(self):
        """
        GIVEN the FirestoreService
        WHEN are passed illegal parameters to update function
        THEN value errors are raised
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreQueryBuilder,
            FirestoreCollectionBuilder,
            FirestoreQueryCondition,
        )

        collection_name = "my_collection"
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        left_hand_side = "l"
        condition = FirestoreQueryCondition.LOWER
        right_hand_side = "r"
        query = (
            FirestoreQueryBuilder()
            .add_condition(
                left_hand_side=left_hand_side,
                condition=condition,
                right_hand_side=right_hand_side,
            )
            .build()
        )

        with self.assertRaises(ValueError):
            Firestore.get(collection=collection_name, query=query)

        with self.assertRaises(ValueError):
            Firestore.get(collection=collection_name, query=left_hand_side)

    @patch(
        "wiser.gcloud.connectors.firestore.firestore_connector.FirestoreConnector.get"
    )
    def test_firestore_get_returns_list_dict(self, firestore_mock):
        """
        GIVEN the FirestoreService
        WHEN a valid get request is performed
        THEN the documents as dict ar retuned
        """
        from wiser.gcloud.services.firestore import Firestore
        from wiser.gcloud.types.firestore import (
            FirestoreQueryBuilder,
            FirestoreCollectionBuilder,
            FirestoreQueryCondition,
        )

        collection_name = "my_collection"
        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name=collection_name)
            .build()
        )
        left_hand_side = "l"
        condition = FirestoreQueryCondition.LOWER
        right_hand_side = "r"
        query = (
            FirestoreQueryBuilder()
            .add_condition(
                left_hand_side=left_hand_side,
                condition=condition,
                right_hand_side=right_hand_side,
            )
            .build()
        )

        stubs = [{"a": "b"} for _ in range(10)]

        firestore_mock.return_value = stubs

        self.assertEqual(Firestore.get(collection=collection, query=query), stubs)
