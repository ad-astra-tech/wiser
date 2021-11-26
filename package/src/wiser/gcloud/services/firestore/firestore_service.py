from typing import List, Dict, Any

from wiser.gcloud.connectors.firestore.firestore_connector import FirestoreConnector
from wiser.gcloud.types.firestore.collection import FirestoreCollection
from wiser.gcloud.types.firestore.document import FirestoreDocument
from wiser.gcloud.types.firestore.query import FirestoreQuery


class Firestore:
    @staticmethod
    def add(collection: FirestoreCollection, document: FirestoreDocument) -> None:
        """
        Adds a document to a collection
        :param collection: the firestore collection
        :param document: the firestore document
        :return: None
        """
        if not isinstance(collection, FirestoreCollection):
            raise ValueError(
                "Passed parameter 'collection' is not a 'FirestoreCollection'"
            )
        if not isinstance(document, FirestoreDocument):
            raise ValueError("Passed parameter 'document' is not a 'FirestoreDocument'")

        FirestoreConnector.add(
            collection_path=collection.collection_name,
            document_id=document.id,
            data=document.data,
        )

    @staticmethod
    def update(collection: FirestoreCollection, document: FirestoreDocument) -> None:
        """
        Updates a document of a collection
        :param collection: the firestore collection
        :param document: the firestore document
        :return: None
        """
        if not isinstance(collection, FirestoreCollection):
            raise ValueError(
                "Passed parameter 'collection' is not a 'FirestoreCollection'"
            )
        if not isinstance(document, FirestoreDocument):
            raise ValueError("Passed parameter 'document' is not a 'FirestoreDocument'")

        if document.id is None:
            raise ValueError("No document id provided")

        FirestoreConnector.update(
            collection_path=collection.collection_name,
            document_id=document.id,
            data=document.data,
        )

    @staticmethod
    def get(
        collection: FirestoreCollection, query: FirestoreQuery
    ) -> List[Dict[Any, Any]]:
        """
        Given a query returns all the documents that match it
        :param collection: the firestore collection
        :param query: the query definition
        :return:
        """
        if not isinstance(collection, FirestoreCollection):
            raise ValueError(
                "Passed parameter 'collection' is not a 'FirestoreCollection'"
            )
        if not isinstance(query, FirestoreQuery):
            raise ValueError("Passed parameter 'query' is not a 'FirestoreQuery'")

        return FirestoreConnector.get(
            collection_name=collection.collection_name,
            where_conditions=query.conditions,
        )
