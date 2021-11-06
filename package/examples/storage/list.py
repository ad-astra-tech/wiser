import os

from massox.gcloud.handlers.storage import StorageHandler
from massox.gcloud.types.storage.location import StorageLocationBuilder

BUCKET_NAME = os.getenv("BUCKET_NAME")

location = StorageLocationBuilder().set_bucket(bucket=BUCKET_NAME).build()
blobs = StorageHandler.get_list_content(location=location)
