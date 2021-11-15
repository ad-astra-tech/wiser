import unittest

class TestAIPlatformService(unittest.TestCase):
    def test_ai_platform_prediction_service(self):
        """
        GIVEN   class AIPlatfrom
        WHEN    accessing at class attribute `prediction`
        THEN    the type is `AIPlatformPrediction`
        """
        from wiser.gcloud.services.ai_platform import AIPlatform
        from wiser.gcloud.services.ai_platform.prediction import AIPlatformPrediction

        self.assertEqual(type(AIPlatform.prediction), AIPlatformPrediction)