<p align="center">
    <img src="https://raw.githubusercontent.com/ad-astra-tech/wiser/main/resources/logo.png" />
</p>
<h2 align="center">Cloud services wrapped wisely</h2>

_Wiser_ is a python package designed to free the developers from the burden of common operations with cloud technologies.
_Wiser_ gives you speed, effectiveness and allows you to truly focus on the application logic.

_Wiser_ comes with several straight-forward high-level interfaces that just work! You don't need to care about the 
underlying infrastructure layer, of the client connections or the data management: _Wiser_ will handle everything for you.

## Installation and usage

### Installation

_Wiser_ is published on [`PyPi`](https://pypi.org/project/wiser/). It requires Python 3.8+. _Wiser_ wraps several cloud
services. Here below you can find wiser sub-packages with the commands to install them:

* [wiser-gcloud-storage](https://github.com/ad-astra-tech/wiser-gcloud-storage): `pip install 'wiser[gcloud-storage]'`
* [wiser-gcloud-firestore](https://github.com/ad-astra-tech/wiser-gcloud-firestore): `pip install 'wiser[gcloud-firestore]'`

### Usage
#### _[wiser-gcloud-storage](https://github.com/ad-astra-tech/wiser-gcloud-storage)_ - Google Cloud Storage
For a complete overview of the APIS exposed by wiser wrapper for Google Cloud Storage it's suggested to check the 
[package example directory](https://github.com/ad-astra-tech/wiser-gcloud-storage/tree/main/examples). Below are shown 
some examples:

```python
import io
import numpy as np
import PyPDF2
from PIL import Image

from wiser.gcloud.storage.services import Storage
from wiser.gcloud.storage.types.location import StorageLocationBuilder

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="path/to/service-account.json"

# Text
location = (
    StorageLocationBuilder()
    .set_bucket(bucket="BUCKET_NAME")
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
Storage.save(obj="This is a sentence I want to save", location=location)
sentence = Storage.get(location=location)

# Numpy array
location = (
    StorageLocationBuilder()
    .set_bucket(bucket="BUCKET_NAME")
    .set_blob_name(blob_name="folder_a/data.npy")
    .build()
)
array = np.array([[1, 2, 3], [1, 2, 3]])
Storage.save(obj=array, location=location)
array = Storage.get(location=location)

# JPG/PNG
image = Image.open("path/to/image.png")
location = (
    StorageLocationBuilder()
    .set_bucket(bucket="BUCKET_NAME")
    .set_blob_name(blob_name="folder_a/data.png")
    .build()
)
Storage.save(obj=image, location=location)
image = Image.open(io.BytesIO(Storage.get(location=location)))

# PDF
pdf_path = "/path/to/file.pdf"
location = (
    StorageLocationBuilder()
    .set_bucket(bucket="BUCKET_NAME")
    .set_blob_name(blob_name="folder_a/data.pdf")
    .build()
)
Storage.save(obj=pdf_path, location=location)
pdf = PyPDF2.PdfFileReader(io.BytesIO(Storage.get(location=location)))
```

#### _[wiser-gcloud-firestore](https://github.com/ad-astra-tech/wiser-gcloud-firestore)_ - Google Cloud Firestore
For a complete overview of the APIS exposed by wiser wrapper for Google Cloud Firestore it's suggested to check the 
[package example directory](https://github.com/ad-astra-tech/wiser-gcloud-firestore/tree/main/examples). Below are shown 
some examples:

```python
from wiser.gcloud.firestore.services import Firestore
from wiser.gcloud.firestore.types import (
    FirestoreCollectionBuilder,
    FirestoreQueryBuilder,
    FirestoreQueryCondition,
    FirestoreQueryDirection,
)

data = {
    "key_1": "value_1",
    "key_2": "xxxx",
    "key_3": {"key_4": "value_4", "key_5": "value_6"},
}
collection = (
    FirestoreCollectionBuilder()
    .set_collection_name(collection_name="COLLECTION_NAME")
    .build()
)
document = (
    FirestoreDocumentBuilder().set_data(data=data).build()
)
Firestore.add(collection=collection, document=document)

query = (
    FirestoreQueryBuilder()
    .add_condition(
        left_hand_side="key_1",
        condition=FirestoreQueryCondition.EQUAL,
        right_hand_side="value_1",
    )
    .add_condition(
        left_hand_side="key_2",
        condition=FirestoreQueryCondition.GREATER,
        right_hand_side="xxxx",
    )
    .add_condition(
        left_hand_side="key_3.key_5",
        condition=FirestoreQueryCondition.NOT_EQUAL,
        right_hand_side="value_6",
    )
    .add_limit(limit=10)
    .add_direction(direction=FirestoreQueryDirection.ASCENDING)
    .build()
)
documents = Firestore.get(collection=collection, query=query)
for document in documents:
    print(document)
```

## Contributions and development

### Contributions
Contributors are welcome! You can either open an issue for a feature request or contact the owner to join the development.

### Development
Development guidelines are:

* **Straightforward APIs**: each module must be designed so to have easy-to-use APIS
* **Default first**: this package targets common operations, so it's ok to do not support fancy configurations
* **Black**: the code is indented with [`black`](https://github.com/psf/black)

    
## Testing
The adopted testing framework is [`unittest`](https://docs.python.org/3/library/unittest.html). To evaluate tests coverage is 
used [`coverage`](https://coverage.readthedocs.io/en/6.1.2/). 

To run unit tests execute:
```shell
coverage run -m --source src/  unittest discover -v
```
And to read the coverage report:
```shell
coverage report -m
```
## License

MIT