from __future__ import annotations


class FirestoreCollection:
    def __init__(self, path: str):
        self.path = path

    @property
    def path(self) -> str:
        return self.path


class FirestoreCollectionBuilder:
    def __init__(self):
        self._path = None

    def set_path(self, path: str) -> FirestoreCollectionBuilder:
        self._path = path

        return self

    def build(self) -> FirestoreCollection:
        if self._path is None:
            raise ValueError("Firestore path not set")
        return FirestoreCollection(path=self._path)
