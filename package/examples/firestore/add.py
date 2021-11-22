from wiser.gcloud.services import Firestore
from wiser.gcloud.types.firestore import (
    FirestoreDocumentBuilder,
    FirestoreCollectionBuilder,
)

data = {"key_1": "value_1", "key_2": "value_2"}
collection = FirestoreCollectionBuilder().set_path(path="collection_path").build()
document = (
    FirestoreDocumentBuilder().set_id(id="my_custom_id").set_data(data=data).build()
)
Firestore.add(collection=collection, document=document)

data = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": {"key_4": "value_4", "key_5": "value_6"},
}
collection = FirestoreCollectionBuilder().set_path(path="collection_path").build()
document = FirestoreDocumentBuilder()
for key, value in data.items():
    document.add_property(key=key, value=value)

document = document.build()
Firestore.add(collection=collection, document=document)
