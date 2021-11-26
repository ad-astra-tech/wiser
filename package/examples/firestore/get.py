from wiser.gcloud.services import Firestore
from wiser.gcloud.types.firestore import (
    FirestoreCollectionBuilder,
    FirestoreQueryBuilder,
    FirestoreQueryCondition,
    FirestoreQueryDirection,
)


COLLECTION_NAME = "collection_name"

collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name=COLLECTION_NAME)
    .build()
)
query = (
    FirestoreQueryBuilder()
    .add_condition(
        left_hand_side="key_1",
        condition=FirestoreQueryCondition.EQUAL,
        right_hand_side="value_1",
    )
    .build()
)
documents = Firestore.get(collection=collection, query=query)
for document in documents:
    print(document)

collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name=COLLECTION_NAME)
    .build()
)
query = (
    FirestoreQueryBuilder()
    .add_condition(
        left_hand_side="key_1",
        condition=FirestoreQueryCondition.EQUAL,
        right_hand_side="value_1",
    )
    .add_condition(
        left_hand_side="key_2",
        condition=FirestoreQueryCondition.EQUAL,
        right_hand_side="xxxx",
    )
    .add_condition(
        left_hand_side="key_3.key_5",
        condition=FirestoreQueryCondition.EQUAL,
        right_hand_side="value_6",
    )
    .add_limit(limit=10)
    .add_direction(direction=FirestoreQueryDirection.ASCENDING)
    .build()
)
documents = Firestore.get(collection=collection, query=query)
for document in documents:
    print(document)
