import os

from google.oauth2 import service_account

AUTH_LOCATION = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

credentials = service_account.Credentials.from_service_account_file(AUTH_LOCATION)
