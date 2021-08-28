import os


def test_save():
    """
    GIVEN Google Storage Handler
    WHEN inking the save() function for saving a txt in bucket: "massox-package-testing", blob_name: "data.txt"
    THEN the file is saved
    """

    # Credentials
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"
    ] = "/home/nicolamassarenti/Documents/Progetti/massox-package/service-account.json"

    # Defining location
    from massox.gcloud.types.storage import StorageLocationBuilder

    cloud_location = (
        StorageLocationBuilder()
        .set_bucket(bucket="massox-package-testing")
        .set_blob_name("data.txt")
        .build()
    )
