import os
from wiser.gcloud.services.ai_platform import AIPlatform

PROJECT_ID = os.getenv("PROJECT_ID")
ENDPOINT = os.getenv("ENDPOINT")
MODEL_NAME = os.getenv("MODEL_NAME")

# Body depends on the signature of your model
body = dict(
    instances=[
        dict(input="This is the first sentence..."),
        dict(input="... and this is the second sentence"),
    ]
)

predictions = AIPlatform.prediction.predict(
    project_id=PROJECT_ID, endpoint=ENDPOINT, model_name=MODEL_NAME, body=body
)
