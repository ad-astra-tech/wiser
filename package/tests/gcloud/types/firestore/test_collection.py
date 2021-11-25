import unittest


class FirestoreCollectionBuilderTest(unittest.TestCase):
    def test_null_collection_name_raise_value_error(self):
        """
        GIVEN the FirestoreCollectionBuilder
        WHEN a None is passed as a collection name
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.collection import FirestoreCollectionBuilder

        with self.assertRaises(ValueError):
            FirestoreCollectionBuilder().set_collection_name(
                collection_name=None
            ).build()

    def test_collection_name_zero_length_raise_value_error(self):
        """
        GIVEN the FirestoreCollectionBuilder
        WHEN a collection name of zero length is set
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.collection import FirestoreCollectionBuilder

        with self.assertRaises(ValueError):
            FirestoreCollectionBuilder().set_collection_name(collection_name="").build()

    def test_collection_name_int_raise_value_error(self):
        """
        GIVEN the FirestoreCollectionBuilder
        WHEN an int is passed as collection_name
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.collection import FirestoreCollectionBuilder

        with self.assertRaises(ValueError):
            FirestoreCollectionBuilder().set_collection_name(collection_name=12).build()

    def test_firestore_collection(self):
        """
        GIVEN a FirestoreCollection
        WHEN  the properties are invoked
        THEN the defined types are returned
        """
        from wiser.gcloud.types.firestore.collection import FirestoreCollectionBuilder

        collection = (
            FirestoreCollectionBuilder()
            .set_collection_name(collection_name="name")
            .build()
        )

        self.assertIsInstance(collection.collection_name, str)
