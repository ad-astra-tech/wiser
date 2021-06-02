from pathlib import Path

from massox.handlers.gcloud.storage.handler import GCloudStorageHandler
from massox.types.gcloud.storage.location import StorageLocationBuilder


storage_handler = GCloudStorageHandler()
bucket = "BUCKET"

text = "This is a sentence to be saved on cloud in a .txt file."

storage_handler.save(
    obj=text,
    location=StorageLocationBuilder()
    .set_bucket(bucket=bucket)
    .set_blob_name("folder_a/folder_b/test_text.txt")
    .build(),
)
