import os

from google.oauth2 import service_account
from src import AUTH_LOCATION


credentials = service_account.Credentials.from_service_account_file(AUTH_LOCATION)
