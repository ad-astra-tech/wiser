from typing import Dict, Union

from google.cloud import firestore


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
