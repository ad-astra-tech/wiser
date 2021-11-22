from __future__ import annotations

from typing import Union, Dict
from copy import deepcopy


class FirestoreDocument:
    def __init__(
        self, id: str, data: Dict[Union[str, int], Union[Dict, int, str, float]]
    ):
        self._id = id
        self._data = data

    @property
    def id(self) -> str:
        return self._id

    @property
    def data(self) -> Dict[Union[str, int], Union[Dict, int, str, float]]:
        return self._data


class FirestoreDocumentBuilder:
    def __init__(self):
        self._id = None

        self._data = None

    def set_id(self, id: str) -> FirestoreDocumentBuilder:
        """
        Sets the document id
        :param id: the document id
        :return: the instance of the builder
        """
        self._id = id
        return self

    def add_property(
        self, key: Union[str, int], value: Union[Dict, int, str, float]
    ) -> FirestoreDocumentBuilder:
        """
        Adds a property to the document
        :param key: the key of the document
        :param value: the value of the document
        :return: the instance of the builder
        """
        if self._data is None:
            self._data = dict()

        self._data[key] = deepcopy(value)

        return self

    def set_data(
        self, data: Dict[Union[str, int], Union[Dict, int, str, float]]
    ) -> FirestoreDocumentBuilder:
        """
        Sets the document.
        :param content: the content of the document
        :return: the instance of the builder
        """
        self._data = deepcopy(data)

        return self

    def build(self) -> FirestoreDocument:
        if self._id is None:
            raise ValueError("Document id not set")
        if self._data is None:
            raise ValueError("Document data not set")

        return FirestoreDocument(id=self._id, data=self._data)
