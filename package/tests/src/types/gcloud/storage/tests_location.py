import pytest


def test_location_builder_no_bucket_raises_valueerror():
    """
    GIVEN LocationBuilder
    WHEN  the bucket is not set
    THEN a value error is raised
    """

    from massox.types.gcloud.storage.location import StorageLocationBuilder

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

    from massox.types.gcloud.storage.location import StorageLocationBuilder

    with pytest.raises(ValueError):
        StorageLocationBuilder().set_bucket(bucket="bucket_name").build()


def test_location_builder_returns_storage_location():
    """
    GIVEN LocationBuilder
    WHEN  the blob name and the bucket are set
    THEN a storage location object is returned
    """

    from massox.types.gcloud.storage.location import StorageLocationBuilder

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

    assert storage_location.get_prefix() == prefix
    assert storage_location.get_bucket() == bucket
    assert storage_location.get_folders() == folders
    assert storage_location.get_filename() == filename
    assert storage_location.get_blob_name() == blob_name
    assert storage_location.get_complete_path() == complete_path