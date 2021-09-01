import pytest

def test_extensions():
    """
    GIVEN FileExtension
    WHEN  the class attributes are checked
    THEN the value is the expected one
    """
    from massox.gcloud.types.data.extensions import FileExtension

    numpy_extension = ".npy"
    json_extension = ".json"
    csv_extension = ".csv"
    text_extension = ".txt"

    assert FileExtension.TEXT == text_extension
    assert FileExtension.JSON == json_extension
    assert FileExtension.CSV == csv_extension
    assert FileExtension.NUMPY == numpy_extension