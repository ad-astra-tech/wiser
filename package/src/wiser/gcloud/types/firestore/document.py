from __future__ import annotations

from typing import Union, Dict
from copy import deepcopy

class FirestoreDocument:
    def __init__(self, id: str, document: Dict[Union[str, int], Union[Dict, int, str, float]]):
        self._id = id
        self._document = document

    @property
    def id(self) -> str:
        return self._id

    @property
    def document(self) -> Dict[Union[str, int], Union[Dict, int, str, float]]:
        return self._document

class FirestoreDocumentBuilder:
    def __init__(self, id: str):
        self._id = id

        self._content = dict()

    def add_property(self, key: Union[str, int], value: Union[Dict, int, str, float]) -> FirestoreDocumentBuilder:
        """
        Adds a property to the document
        :param key: the key of the document
        :param value: the value of the document
        :return: the instance of the builder
        """
        self._content[key] = deepcopy(value)

        return self

    def set_document(self, content: Dict[Union[str, int], Union[Dict, int, str, float]]) -> FirestoreDocumentBuilder:
        """
        Sets the document.
        :param content: the content of the document
        :return: the instance of the builder
        """
        self._content = deepcopy(content)

        return self

    def build(self) -> FirestoreDocument:
        return FirestoreDocument(
            id=self._id,
            document=self._content
        )
