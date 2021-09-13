import unittest


class StorageLocationTest(unittest.TestCase):
    def test_location_builder_no_bucket_raises_valueerror(self):
        """
        GIVEN StorageLocationBuilder
        WHEN  the bucket is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.storage.location import StorageLocationBuilder

        with self.assertRaises(ValueError):
            StorageLocationBuilder().set_blob_name(
                blob_name="folder_a/folder_b/filename"
            ).build()

    def test_location_builder_no_blobname_raises_valueerror(self):
        """
        GIVEN StorageLocationBuilder
        WHEN  the blob name is not set
        THEN a value error is raised
        """

        from massox.gcloud.types.storage.location import StorageLocationBuilder

        with self.assertRaises(ValueError):
            StorageLocationBuilder().set_bucket(bucket="bucket_name").build()

    def test_location_builder_returns_storage_location(self):
        """
        GIVEN LocationBuilder
        WHEN  the blob name and the bucket are set
        THEN a fully featured storage location object is returned
        """

        from massox.gcloud.types.storage.location import StorageLocationBuilder

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

        self.assertEqual(storage_location.prefix, prefix)
        self.assertEqual(storage_location.bucket, bucket)
        self.assertEqual(storage_location.folders, folders)
        self.assertEqual(storage_location.filename, filename)
        self.assertEqual(storage_location.blob_name, blob_name)
        self.assertEqual(storage_location.complete_path(), complete_path)
