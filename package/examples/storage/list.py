import os

from massox.gcloud.handlers.storage import StorageHandler
from massox.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")

# Listing content of a bucket
location = StorageLocationBuilder().set_bucket(bucket=BUCKET_NAME).build()
blobs = StorageHandler.get_list_content(location=location)
for blob in blobs:
    print(blob.complete_path())

# Listing content of a specific folder
location = (
    StorageLocationBuilder()
    .set_bucket(bucket=BUCKET_NAME)
    .set_blob_name(blob_name="folder_a")
    .build()
)
blobs = StorageHandler.get_list_content(location=location)
for blob in blobs:
    print(blob.complete_path())
