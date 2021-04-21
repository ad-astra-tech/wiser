import os
import json

class AuthenticationManager:
    def __init__(self):
        self.__auth = None

    def __set_from_env_variable(self) -> None:
        # Checking if exists the env variable
        if os.getenv("GOOGLE_APPLICATION_CREDENTIALS") != None:
            self.__auth = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    def from_service_account(self, path: str) -> None:
        # Checking if it's a valid file
        if not os.path.exists():
            raise FileNotFoundError("File {file} does not exists".format(file=path))

        self.__auth = path

    def is_compiled(self) -> bool:
        if self.__auth is None:
            # Checking again if exists env variable
            self.__set_from_env_variable()

        return  self.__auth != None

authentication_manager = AuthenticationManager()