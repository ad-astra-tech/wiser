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

    def add_condition(
        self,
        left_hand_side: str,
        condition: Union[str, FirestoreQueryCondition],
        right_hand_side: Any,
    ) -> FirestoreQueryBuilder:

        if not isinstance(left_hand_side, str):
            raise ValueError("Left hand side operator accepts only strings")
        if not isinstance(condition, str) and not isinstance(
            condition, FirestoreQueryCondition
        ):
            raise ValueError(
                "Condition operator accepts only strings or FirestoreQueryCondition"
            )

        condition_str = condition
        if isinstance(condition, FirestoreQueryCondition):
            condition_str = condition.value

        self._conditions.append((left_hand_side, condition_str, right_hand_side))

        return self

    def add_limit(self, limit: int) -> FirestoreQueryBuilder:
        if not isinstance(limit, int):
            raise ValueError("Limit must be an integer")

        self._limit = limit
        return self

    def add_order_by(self, by: str) -> FirestoreQueryBuilder:
        self._order_by = by

        return self

    def add_direction(
        self, direction: Union[str, FirestoreQueryDirection]
    ) -> FirestoreQueryBuilder:
        if not isinstance(direction, str) and not isinstance(
            direction, FirestoreQueryDirection
        ):
            raise ValueError("Direction must be string or FirestoreQueryDirection")

        direction_str = direction
        if isinstance(direction, FirestoreQueryDirection):
            direction_str = direction.value

        self._direction = direction

        return self

    def build(self) -> FirestoreQuery:
        return FirestoreQuery(
            conditions=self._conditions,
            limit=self._limit,
            order_by=self._order_by,
            direction=self._direction,
        )
