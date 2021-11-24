from __future__ import annotations


class FirestoreCollection:
    def __init__(self, collection_name: str):
        self._collection_name = collection_name

    @property
    def collection_name(self) -> str:
        return self._collection_name


class FirestoreCollectionBuilder:
    def __init__(self):
        self._collection_name = None

    def set_collection_name(self, collection_name: str) -> FirestoreCollectionBuilder:
        self._collection_name = collection_name

        return self

    def build(self) -> FirestoreCollection:
        if self._collection_name is None:
            raise ValueError("Firestore path not set")
        return FirestoreCollection(collection_name=self._collection_name)
