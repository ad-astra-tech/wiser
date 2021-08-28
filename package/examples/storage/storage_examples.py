from massox.gcloud.handlers.storage import StorageHandler
from massox.gcloud.types.storage.location import StorageLocationBuilder

sentence = "This is a sentence I want to upload on Google Cloud Storage"

location = (
    StorageLocationBuilder()
    .set_bucket(bucket="bucket-name")
    .set_blob_name(blob_name="folder_a/folder_b/sentence.txt")
    .build()
)
StorageHandler.save(obj=sentence, location=location)