from __future__ import annotations

from typing import Union, Dict, Any
from copy import deepcopy


class FirestoreDocument:
    def __init__(self, id: str, data: Dict[Union[str, int], Any]):
        self._id = id
        self._data = data

    @property
    def id(self) -> str:
        return self._id

    @property
    def data(self) -> Dict[Union[str, int], Any]:
        return self._data


class FirestoreDocumentBuilder:
    def __init__(self):
        self._id = None

        self._data = None

    def __validate(self) -> None:
        """
        Performs data validation
        :return: None
        """
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("Parameter 'id' must be a string")

        if self._data is None:
            raise ValueError("Document data not set")
        elif not isinstance(self._data, dict):
            raise ValueError("Document data must be a dict")
        else:
            for key, _ in self._data.items():
                if not isinstance(key, int) and not isinstance(key, str):
                    raise ValueError(
                        "Keys of first level of data must be integers or strings"
                    )

    def set_id(self, id: str) -> FirestoreDocumentBuilder:
        """
        Sets the document id
        :param id: the document id
        :return: the instance of the builder
        """
        self._id = id
        return self

    def add_property(
        self, key: Union[str, int], value: Any
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

    def set_data(self, data: Dict[Union[str, int], Any]) -> FirestoreDocumentBuilder:
        """
        Sets the document.
        :param content: the content of the document
        :return: the instance of the builder
        """
        self._data = deepcopy(data)

        return self

    def build(self) -> FirestoreDocument:
        self.__validate()

        return FirestoreDocument(id=self._id, data=self._data)
