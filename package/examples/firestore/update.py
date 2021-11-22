from wiser.gcloud.services import Firestore
from wiser.gcloud.types.firestore import (
    FirestoreDocumentBuilder,
    FirestoreCollectionBuilder,
)

# ...Supposing that document with id "my_custom_id" already exists

data = {"key_1": "value_1", "key_2": "value_4"}
collection = FirestoreCollectionBuilder().set_path(path="collection_path").build()
document = (
    FirestoreDocumentBuilder().set_id(id="my_custom_id").set_data(data=data).build()
)
Firestore.update(collection=collection, document=document)
data = {"key_1": "foo", "key_2": "boo"}
collection = FirestoreCollectionBuilder().set_path(path="collection_path").build()
document = FirestoreDocumentBuilder()
for key, value in data.items():
    document.add_property(key=key, value=value)

document = document.set_id(id="my_custom_id")
document = document.build()
Firestore.update(collection=collection, document=document)
