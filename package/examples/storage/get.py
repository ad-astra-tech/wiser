import os

from massox.gcloud.services.storage import Storage
from massox.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")

# Text
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
text = Storage.get(location=location)

# Numpy array
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/data.npy")
    .build()
)
array = Storage.get(location=location)

# JSON
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a/folder_c/data.json")
    .build()
)

data = Storage.get(location=location)