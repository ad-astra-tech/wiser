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
            FirestoreCollectionBuilder().set_collection_name(collection_name=None).build()

    def test_collection_name_zero_length_raise_value_error(self):
        """
        GIVEN the FirestoreCollectionBuilder
        WHEN a collection name of zero length is set
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.collection import FirestoreCollectionBuilder

        with self.assertRaises(ValueError):
            FirestoreCollectionBuilder().set_collection_name(collection_name="").build()