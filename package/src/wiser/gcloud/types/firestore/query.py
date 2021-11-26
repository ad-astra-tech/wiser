from __future__ import annotations

from enum import Enum
from typing import Union, List, Tuple, Any


class FirestoreQueryCondition(Enum):
    GREATER = ">"
    LOWER = "<"
    GREATER_EQUAL_TO = ">="
    LOWER_EQUAL_TO = "<="
    EQUAL = "=="
    NOT_EQUAL = "!="
    ARRAY_CONTAINS = "array_contains"


class FirestoreQueryDirection(Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class FirestoreQuery:
    def __init__(
        self,
        conditions: List[Tuple[str, str, Any]],
        limit: int,
        order_by: str,
        direction: str,
    ):
        self._conditions = conditions
        self._limit = limit
        self._order_by = order_by
        self._direction = direction

    @property
    def conditions(self) -> List[Tuple[str, str, Any]]:
        return self._conditions

    @property
    def limit(self) -> int:
        return self._limit

    @property
    def order_by(self) -> str:
        return self._order_by

    @property
    def direction(self) -> str:
        return self._direction


class FirestoreQueryBuilder:
    def __init__(self):
        self._conditions = []
        self._limit = None
        self._order_by = None
        self._direction = None

    def __validate(self) -> None:
        """
        Performs data validation
        :return: None
        """
        # conditions
        for condition in self._conditions:
            (left_hand_side, condition_operator, right_hand_side) = condition

            if not isinstance(left_hand_side, str):
                raise ValueError("Left hand side of a condition must be a string")

            if not isinstance(condition_operator, str) and not isinstance(
                condition_operator, FirestoreQueryCondition
            ):
                raise ValueError(
                    "Condition operator must be a string or a FirestoreQueryCondition"
                )
            if isinstance(condition_operator, str) and not condition_operator in [
                op.value for op in FirestoreQueryCondition
            ]:
                raise ValueError(
                    "Condition operator string must match one of the values of FirestoreQueryOperator"
                )
        # direction
        if (
            self._direction is not None
            and not isinstance(self._direction, str)
            and not isinstance(self._direction, FirestoreQueryDirection)
        ):
            raise ValueError("Direction must be string or FirestoreQueryDirection")

        # limit
        if self._limit is not None:
            if not isinstance(self._limit, int):
                raise ValueError("Limit must be an integer")
            if self._limit < 0:
                raise ValueError("Limit must be greater or equal to zero")

    def add_condition(
        self,
        left_hand_side: str,
        condition: Union[str, FirestoreQueryCondition],
        right_hand_side: Any,
    ) -> FirestoreQueryBuilder:

        self._conditions.append((left_hand_side, condition, right_hand_side))

        return self

    def add_limit(self, limit: int) -> FirestoreQueryBuilder:

        self._limit = limit
        return self

    def add_order_by(self, by: str) -> FirestoreQueryBuilder:
        self._order_by = by

        return self

    def add_direction(
        self, direction: Union[str, FirestoreQueryDirection]
    ) -> FirestoreQueryBuilder:

        direction_str = direction
        if isinstance(direction, FirestoreQueryDirection):
            direction_str = direction.value

        self._direction = direction_str

        return self

    def build(self) -> FirestoreQuery:
        self.__validate()

        return FirestoreQuery(
            conditions=self._conditions,
            limit=self._limit,
            order_by=self._order_by,
            direction=self._direction,
        )
