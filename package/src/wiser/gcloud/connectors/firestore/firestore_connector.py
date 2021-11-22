from google.cloud import firestore

from wiser.gcloud.types.firestore.collection import FirestoreCollection
from wiser.gcloud.types.firestore.document import FirestoreDocument


class FirestoreConnector:
    def add(self, collection: FirestoreCollection, document: FirestoreDocument) -> None:
        """
        Adds a document to a collection
        :param collection: a firestore collection
        :param document: a firestore document
        :return: None
        """

        firestore.Client().collection(collection.path).document(document_id=document.id)