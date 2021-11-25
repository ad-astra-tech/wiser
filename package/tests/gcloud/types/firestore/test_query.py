import unittest


class FirestoreQueryBuilderTest(unittest.TestCase):
    def test_limit_invalid_raises_value_error(self):
        """
        GIVEN a FirestoreQueryBuilder
        WHEN is set an invalid limit
        THEN value error is set
        """
        from wiser.gcloud.types.firestore.query import (
            FirestoreQueryBuilder,
            FirestoreQueryCondition,
        )

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key",
                condition=FirestoreQueryCondition.LOWER,
                right_hand_side=3,
            ).add_limit(limit="3").build()

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key",
                condition=FirestoreQueryCondition.LOWER,
                right_hand_side=3,
            ).add_limit(limit=3.33).build()

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key",
                condition=FirestoreQueryCondition.LOWER,
                right_hand_side=3,
            ).add_limit(limit=-3).build()

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key",
                condition=FirestoreQueryCondition.LOWER,
                right_hand_side=3,
            ).add_limit(limit=[3]).build()

    def test_limit_valid_return_firestore_query(self):
        """
        GIVEN a FirestoreQueryBuilder
        WHEN is set a valid limit
        THEN a FirestoreQuery instance is returned
        """
        from wiser.gcloud.types.firestore.query import (
            FirestoreQueryBuilder,
            FirestoreQueryCondition,
            FirestoreQuery,
        )

        self.assertIsInstance(
            FirestoreQueryBuilder()
            .add_condition(
                left_hand_side="key",
                condition=FirestoreQueryCondition.LOWER,
                right_hand_side=3,
            )
            .add_limit(limit=3)
            .build(),
            FirestoreQuery,
        )

    def test_add_condition_raises_value_error(self):
        """
        GIVEN a FirestoreQueryBuilder
        WHEN are added invalid conditions
        THEN value error is raised
        """
        from wiser.gcloud.types.firestore.query import FirestoreQueryBuilder

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key_1", condition="12345", right_hand_side="value_1"
            ).build()

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="key_1", condition=12345, right_hand_side="value_1"
            ).build()

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side=2, condition="12345", right_hand_side=3
            ).build()

    def test_non_valid_direction_raises_value_error(self):
        """
        GIVEN a FirestoreQueryBuilder
        WHEN a non valid direction is given
        THEN a value error is raised
        """
        from wiser.gcloud.types.firestore.query import (
            FirestoreQueryBuilder,
            FirestoreQueryDirection,
        )

        with self.assertRaises(ValueError):
            FirestoreQueryBuilder().add_condition(
                left_hand_side="k", condition="==", right_hand_side="h"
            ).add_direction(direction=10293).build()

    def test_firestore_query_props(self):
        """
        GIVEN a valid FirestoreQueryBuilder
        WHEN evaluated proprs of FirestoreQUery
        THEN all the values are the expected
        """
        from wiser.gcloud.types.firestore.query import (
            FirestoreQueryBuilder,
            FirestoreQueryDirection,
        )

        conditions = [
            ("key_1", "==", "value_1"),
            ("key_2", "!=", "value_2"),
            ("key_3", ">=", "value_3"),
        ]
        limit = 10
        order_by = "key_2"
        direction = FirestoreQueryDirection.ASCENDING

        query = FirestoreQueryBuilder()
        for condition in conditions:
            query.add_condition(
                left_hand_side=condition[0],
                condition=condition[1],
                right_hand_side=condition[2],
            )
        query.add_limit(limit=limit)
        query.add_direction(direction=direction)
        query.add_order_by(by=order_by)

        query = query.build()

        self.assertEqual(query.conditions, conditions)
        self.assertEqual(query.limit, limit)
        self.assertEqual(query.order_by, order_by)
        self.assertEqual(query.direction, direction.value)
