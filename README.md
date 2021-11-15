<p align="center">
    <img src="https://raw.githubusercontent.com/nicolamassarenti/wiser/dev/resources/logo.png" />
</p>
<h2 align="center">The cloud enabler</h2>

_Wiser_ is a python package designed to free the developers from the burden of common operations with cloud technologies.
_Wiser_ gives you speed, effectiveness and allows you to truly focus on the application logic.

_Wiser_ comes with several straight-forward high-level interfaces that just work! You don't need to care about the 
underlying infrastructure layer, of the client connections or the data management: _Wiser_ will handle everything for you.

## Installation and usage

### Installation

_Wiser_ can be installed by running `pip install wiser`. It requires Python 3.8+.

### Usage
_Wiser_ comes with several examples: you can find them in the [examples folder](https://github.com/nicolamassarenti/wiser/tree/main/package/examples/). A brief examples of the services currently supported is shown in the following.

#### Google Cloud Storage
GCP Storage supported types are: `.txt`, `.json`, `.npy`, `.jpg` and `.png`. Below is shown some examples of the `get()` and `save()` APIs.

```python
import io
import os
import numpy as np
from PIL import Image
from wiser.gcloud.services.storage import Storage
from wiser.gcloud.types.storage.location import StorageLocationBuilder

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/service-account.json"

location = (
    StorageLocationBuilder()
        .set_bucket(bucket="BUCKET_NAME")
        .set_blob_name(blob_name="path/to/sentence.txt")
        .build()
)
text = Storage.get(location=location)

location = (
    StorageLocationBuilder()
        .set_bucket(bucket=BUCKET_NAME)
        .set_blob_name(blob_name="path/to/array.npy")
        .build()
)
array = np.array(
    [[1, 2, 3], [1, 2, 3]]
)
Storage.save(obj=array, location=location)

image = Image.open("path/to/image.png")  # accepted also extension .jpg
location = (
    StorageLocationBuilder()
        .set_bucket(bucket=BUCKET_NAME)
        .set_blob_name(blob_name="folder_a/data.png")
        .build()
)

Storage.save(obj=image, location=location)
image = Image.open(
    io.BytesIO(
        Storage.get(location=location)
    )
)
```

#### AI Platform
At this time is supported only the `prediction` API of `AI Platform`. When building the body it's important to respect
model signature. More information [here](https://blog.tensorflow.org/2021/03/a-tour-of-savedmodel-signatures.html).
```python
import os
from wiser.gcloud.services.ai_platform import AIPlatform

# Body depends on the signature of your model
body = dict(
    instances=[
        dict(input="This is the first sentence..."),
        dict(input="... and this is the second sentence")
    ]
)

predictions = AIPlatform.prediction.predict(
    project_id="PROJECT_ID",
    endpoint="ENDPOINT",
    model_name="MODEL_NAME",
    body=body
)
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
coverage run -m --source src/  unittest discover
```
And to read the coverage report:
```shell
coverage report -m
```
## License

MIT