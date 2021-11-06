import os

import numpy as np

from massox.gcloud.handlers.storage import StorageHandler
from massox.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")

# Text
text_location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
text = StorageHandler.get(location=text_location)

# Numpy array
np_location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/data.npy")
    .build()
)
array = StorageHandler.get(location=np_location)

print("A")
