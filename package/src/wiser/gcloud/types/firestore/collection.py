from __future__ import annotations

class FirestoreCollection:
    def __init__(self, path: str):
        self.path = path

    @property
    def path(self) -> str:
        return self.path

class FirestoreCollectionBuilder:
    def __init__(self, path: str):
        self._path = path

    def build(self) -> FirestoreCollection:
        return FirestoreCollection(
            path=self._path
        )
