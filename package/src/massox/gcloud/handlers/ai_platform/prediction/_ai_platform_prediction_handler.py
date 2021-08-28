import googleapiclient.discovery

from google.api_core.client_options import ClientOptions


class AIPlatformPredictionHandler:
    @staticmethod
    def predict(
        project_id: str, endpoint: str, model_name: str, body: dict, version: str = None
    ):
        client_options = ClientOptions(api_endpoint=endpoint)
        client = googleapiclient.discovery.build(
            "ml", "v1", client_options=client_options
        )

        name = "projects/{project_id}/models/{model_name}".format(
            project_id=project_id, model_name=model_name
        )

        if version is not None:
            name += "/versions/{version}".format(version=version)

        response = client.projects().predict(name=name, body=body).execute()

        if "error" in response:
            raise RuntimeError(response["error"])

        return response["predictions"]
