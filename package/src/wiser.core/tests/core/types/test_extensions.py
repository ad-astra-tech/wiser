import unittest


class ExtensionTest(unittest.TestCase):
    def test_extensions(self):
        """
        GIVEN FileExtension
        WHEN  the class attributes are checked
        THEN the value is the expected one
        """
        from wiser.gcloud.types.data.extensions import FileExtension

        numpy_extension = ".npy"
        json_extension = ".json"
        csv_extension = ".csv"
        text_extension = ".txt"

        self.assertEqual(FileExtension.TEXT, text_extension)
        self.assertEqual(FileExtension.JSON, json_extension)
        self.assertEqual(FileExtension.CSV, csv_extension)
        self.assertEqual(FileExtension.NUMPY, numpy_extension)
