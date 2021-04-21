import os
import json

class AuthenticationManager:
    def __init__(self):
        self.__auth = None
        self.__is_env = False
        self.__is_path_to_service_account = False
        self.__is_json = False

        self.__set_from_env_variable()

    def __set_from_env_variable(self) -> None:
        # Checking if exists the env variable
        if os.getenv("GOOGLE_APPLICATION_CREDENTIALS") != None:
            tmp_auth = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

            if os.path.exists(tmp_auth):
                # If the ENV variable is a file and points to an existing file, I consider it the path to the service account
                print("Env variable {tmp_auth} is a path")
                self.__auth = tmp_auth
                self.__is_path_to_service_account = True
            else:
                # If the ENV variabel is a valid json, I consider it the content of the service account
                try:
                    tmp_auth = json.loads(tmp_auth)
                    print("Env variable {tmp_auth} is a valid json")
                except:
                    print("Env variable {tmp_auth} is not a valid json")

    def from_service_account(self, path: str) -> None:
        # Checking if it's a valid file
        if not os.path.exists():
            raise FileNotFoundError("File {file} does not exists".format(file=path))

        print("Setting {path} as service account location".format(path=path))
        self.__auth = path
        self.__is_path_to_service_account = True

    def is_path(self) -> bool:
        return self.__is_path_to_service_account

    def is_json(self) -> bool:
        return self.__is_json

    def is_env(self) -> bool:
        return self.__is_env

