import os

import numpy as np

from massox.gcloud.handlers.storage import StorageHandler
from massox.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")

# Text
sentence = "This is a sentence I want to upload on Google Cloud Storage"
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
StorageHandler.save(obj=sentence, location=location)

# Numpy array
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/data.npy")
    .build()
)
StorageHandler.save(obj=np.array([[1, 2, 3], [1, 2, 3]]), location=location)

# JSON
data = {
    "key_1": "value_1",
    "key_2": "value_2"
}
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_c/data.json")
    .build()
)
StorageHandler.save(obj=data, location=location)