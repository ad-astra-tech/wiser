from wiser.gcloud.connectors.firestore.firestore_connector import FirestoreConnector
from wiser.gcloud.types.firestore.collection import FirestoreCollection
from wiser.gcloud.types.firestore.document import FirestoreDocument


class Firestore:
    @staticmethod
    def add(collection: FirestoreCollection, document: FirestoreDocument) -> None:
        """
        Adds a document to a collection
        :param collection: the firestore collection
        :param document: the firestore document
        :return: None
        """
        if type(collection) is not type(FirestoreCollection):
            raise TypeError(
                "Passed parameter 'collection' is not a 'FirestoreCollection'"
            )
        if type(document) is not type(FirestoreDocument):
            raise TypeError("Passed parameter 'document' is not a 'FirestoreDocument'")

        FirestoreConnector.add(
            collection_path=collection.path, document_id=document.id, data=document.data
        )
