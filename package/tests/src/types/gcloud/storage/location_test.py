import pytest


def test_location_builder_no_bucket_raises_valueerror():
    """
    GIVEN LocationBuilder
    WHEN  the bucket is not set
    THEN a value error is raised
    """

    from massox.gcloud.types.storage import StorageLocationBuilder

    with pytest.raises(ValueError):
        StorageLocationBuilder().set_blob_name(
            blob_name="folder_a/folder_b/filename"
        ).build()


def test_location_builder_no_blobname_raises_valueerror():
    """
    GIVEN LocationBuilder
    WHEN  the blob name is not set
    THEN a value error is raised
    """

    from massox.gcloud.types.storage import StorageLocationBuilder

    with pytest.raises(ValueError):
        StorageLocationBuilder().set_bucket(bucket="bucket_name").build()


def test_location_builder_returns_storage_location():
    """
    GIVEN LocationBuilder
    WHEN  the blob name and the bucket are set
    THEN a storage location object is returned
    """

    from massox.gcloud.types.storage import StorageLocationBuilder

    prefix = "gs://"
    bucket = "bucket_name"
    filename = "filename.json"
    folders = "folder_a"
    blob_name = folders + "/" + filename
    complete_path = prefix + bucket + "/" + blob_name

    storage_location = (
        StorageLocationBuilder()
        .set_bucket(bucket=bucket)
        .set_blob_name(blob_name="folder_a/filename.json")
        .build()
    )

    assert storage_location.prefix == prefix
    assert storage_location.bucket == bucket
    assert storage_location.folders == folders
    assert storage_location.filename == filename
    assert storage_location.blob_name == blob_name
    assert storage_location.complete_path == complete_path
