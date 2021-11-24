from wiser.gcloud.services import Firestore
from wiser.gcloud.types.firestore import (
    FirestoreDocumentBuilder,
    FirestoreCollectionBuilder,
)

COLLECTION_NAME = "collection_name"

data = {"key_1": "value_1", "key_2": "value_2"}
collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name=COLLECTION_NAME)
    .build()
)
document = (
    FirestoreDocumentBuilder().set_id(id="my_custom_id").set_data(data=data).build()
)
Firestore.add(collection=collection, document=document)

data = {
    "key_1": "value_1",
    "key_2": "xxxx",
    "key_3": {"key_4": "value_4", "key_5": "value_6"},
}
collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name=COLLECTION_NAME)
    .build()
)
document = FirestoreDocumentBuilder()
for key, value in data.items():
    document.add_property(key=key, value=value)

document = document.build()
Firestore.add(collection=collection, document=document)
