import os

import numpy as np

from PIL import Image

from wiser.gcloud.services.storage import Storage
from wiser.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="path/to/service-account.json"

# Text
sentence = "This is a sentence I want to upload on Google Cloud Storage"
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
Storage.save(obj=sentence, location=location)

# Numpy array
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/data.npy")
    .build()
)
Storage.save(obj=np.array([[1, 2, 3], [1, 2, 3]]), location=location)

# PDF location
pdf_path = "/path/to/file.pdf"
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/data.pdf")
    .build()
)
Storage.save(obj=pdf_path, location=location)
