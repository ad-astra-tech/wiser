from typing import Dict, Union, Any, List, Tuple

from google.cloud import firestore

firestore_timestamp = firestore.SERVER_TIMESTAMP


class FirestoreConnector:
    @staticmethod
    def add(
        collection_path: str,
        document_id: str,
        data: Dict[Union[str, int], Union[Dict, int, str, float]],
    ) -> None:
        """
        Adds a document to a collection
        :param collection_path: the firestore collection path
        :param document_id: the firestore document id
        :param data: the content of the document
        :return: None
        """

        firestore.Client().collection(collection_path).document(
            document_id=document_id
        ).set(document_data=data)

    @staticmethod
    def update(
        collection_path: str,
        document_id: str,
        data: Dict[Union[str, int], Union[Dict, int, str, float]],
    ) -> None:
        """
        Updates a document of a collection
        :param collection_path: the firestore collection path
        :param document_id: the firestore document id
        :param data: the content of the document
        :return: None
        """

        firestore.Client().collection(collection_path).document(
            document_id=document_id
        ).update(field_updates=data)

    @staticmethod
    def get(
        collection_name: str,
        where_conditions: List[Tuple[str, str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Given a query, returns the documents that match it
        :param collection_name: the firestore collection name
        :param where_conditions: the list of where condirtions
        :return: the list of results as dict
        """
        query_results = []
        collection = firestore.Client().collection(collection_name)
        for condition in where_conditions:
            collection = collection.where(
                field_path=condition[0], op_string=condition[1], value=condition[2]
            )
        docs = collection.stream()

        for doc in docs:
            query_results.append(doc.to_dict())

        return query_results
