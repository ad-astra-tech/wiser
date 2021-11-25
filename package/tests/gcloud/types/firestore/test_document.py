import unittest


class FirestoreDocumentBuilderTest(unittest.TestCase):
    def test_id_not_string_raises_value_error(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN  the id is not a string
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.document import FirestoreDocumentBuilder

        with self.assertRaises(ValueError):
            doc = FirestoreDocumentBuilder().set_id(id=12).build()

    def test_id_null_no_error_is_raised(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN is passed a null id
        THEN no value error is raised
        """
        from wiser.gcloud.types.firestore.document import (
            FirestoreDocumentBuilder,
            FirestoreDocument,
        )

        self.assertIsInstance(
            FirestoreDocumentBuilder().set_id(id=None).set_data({"a": 3}).build(),
            FirestoreDocument,
        )

    def test_no_data_error_is_raised(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN no data is set
        THEN a value error is raised
        """
        from wiser.gcloud.types.firestore.document import (
            FirestoreDocumentBuilder,
        )

        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_id(id=None).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().build()

    def test_data_not_dict_error_is_raised(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN not a dictionary is set as data
        THEN a value error is raised
        """
        from wiser.gcloud.types.firestore.document import (
            FirestoreDocumentBuilder,
        )

        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data=123).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data=(1, 2, 3)).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data=[1, 2, 3]).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data=1.23).build()

    def test_add_property_with_invalid_keys_raises_value_error(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN is added data with an illegal key
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.document import FirestoreDocumentBuilder

        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().add_property(key=1, value=2).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().add_property(key=None, value=2).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().add_property(key=[1.23], value=2).build()

    def test_add_property_with_invalid_keys_raises_value_error(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN is added a property with an illegal key
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.document import FirestoreDocumentBuilder

        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data={0.0002: 3}).build()
        with self.assertRaises(ValueError):
            FirestoreDocumentBuilder().set_data(data={None: 3}).build()

    def test_add_property_with_valid_keys_build_firestore_document(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN is added data with a legal key
        THEN when built a firestore document is returned
        """
        from wiser.gcloud.types.firestore.document import (
            FirestoreDocumentBuilder,
            FirestoreDocument,
        )

        self.assertIsInstance(
            FirestoreDocumentBuilder().add_property(key="123", value="321").build(),
            FirestoreDocument,
        )
        self.assertIsInstance(
            FirestoreDocumentBuilder().add_property(key=123, value="321").build(),
            FirestoreDocument,
        )

    def test_add_id_returns_valid_firestore_document(self):
        """
        GIVEN the FirestoreDocumentBuilder
        WHEN is set a valid id and added data
        THEN a FirestoreDocument instance is returned
        """
        from wiser.gcloud.types.firestore.document import (
            FirestoreDocumentBuilder,
            FirestoreDocument,
        )

        doc_id = "test"
        data = {"a": 123}
        doc = FirestoreDocumentBuilder().set_id(id=doc_id).set_data(data=data).build()

        self.assertIsInstance(doc, FirestoreDocument)

        self.assertEqual(doc._id, doc_id)
        self.assertEqual(doc._data, data)
        self.assertEqual(doc.id, doc_id)
        self.assertEqual(doc.data, data)
