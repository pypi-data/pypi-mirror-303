import requests
import threading
from EscrowAICI.algo_owner import (
    upload_algo_version,
    finish_algo_upload,
    upload_algo,
    get_algo_notification,
)
from EscrowAICI.encryption import encrypt_algo
from EscrowAICI.checks import algo_check
import os
import base64
import jwt
import datetime


def threaded(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    return wrapper


class EscrowAI:
    # public variables

    user = ""
    project = ""
    org = ""
    env = ""
    compute = ""
    ao = True  # For now, User is AO

    # private variables

    __token = ""
    __cek = ""
    __auth_key = ""

    __auth_audience = {
        "dev": {"audience": "dev.api.beekeeperai"},
        "tst": {"audience": "testing.api.beekeeperai"},
        "stg": {"audience": "staging.api.beekeeperai"},
        "prod": {"audience": ""},
    }

    # constructor

    def __init__(
        self, authKey: str, project_id: str, organization_id: str, environment="prod"
    ):
        self.env = environment
        self.project = project_id
        self.org = organization_id
        self.__get_auth_key(self, authKey)
        self.__login(self.__auth_key)
        # self.__get_user()
        self.get_cek()
        self.compute = self.__get_compute()
        self.type = self.__get_type()

    # public methods

    # # encryption methods

    # private methods

    def __get_auth_key(self, b64encoded_priv_key: str):
        self.__auth_key = base64.b64decode(b64encoded_priv_key)

    def __login(self, key: str):
        # Generate JWT
        try:
            payload = {
                "iss": "EscrowAI-SDK",  # Issuer
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(minutes=5),  # Expiration
                "aud": self.__auth_audience.get(self.env).get("audience"),  # Audience
                "sub": self.project,  # Subject (user ID)
            }

            # Sign JWT with private key
            token = jwt.encode(payload, key, algorithm="RS256")

            self.__token = token
        except Exception as e:
            raise Exception(f"Error siging jwt with auth key: {e}")

    def __get_compute(self):
        response = requests.get(
            f"https://frontoffice.{self.env}.escrow.beekeeperai.com/project/"
            + self.project
            + "/",
            headers={
                "Content-type": "application/json",
                "Authorization": "Bearer " + self.__token,
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
            },
        )

        return response.json()["confidential_compute_technology"]

    def __get_type(self):
        response = requests.get(
            f"https://frontoffice.{self.env}.escrow.beekeeperai.com/project/"
            + self.project
            + "/",
            headers={
                "Content-type": "application/json",
                "Authorization": "Bearer " + self.__token,
                "User-Agent": "curl/7.71.1",
            },
        )

        return response.json()["project_model_type"]

    def __refresh_token(self):
        if len(self.__auth_key) > 1:
            self.__login(self.__auth_key)
        else:
            raise Exception("Error: Couldn't find an auth key..")

    def get_cek(self):
        encoded_key = os.environ.get("CONTENT_ENCRYPTION_KEY")
        decoded_key = base64.b64decode(encoded_key)
        self.__cek = decoded_key

    def encrypt_algo(self, directory: str, key_from_file=False, secret=""):
        if key_from_file:
            with open(secret, "rb") as read:
                key = read.read()
            encrypt_algo(directory, key)
        else:
            encrypt_algo(directory, self.__cek)

    @threaded
    def upload_algorithm(
        self,
        filename: str,
        name: str,
        algo_type="validation",
        version="v1",
        memory=4,
        description="null",
        notification=True,
    ):
        self.__refresh_token()

        if self.type == "validation" and algo_type != self.type:
            raise Exception("Validation projects can only have validation algorithms")

        exists = algo_check(self.env, self.project, self.__token)
        if exists:
            response = upload_algo_version(
                self.env,
                self.project,
                exists[1],
                version,
                description,
                self.compute,
                algo_type,
                filename,
                self.__token,
            )
            if response.status_code != 201:
                raise Exception(f"Error: {response.status_code} \n{response.text}")
            final_response = finish_algo_upload(
                self.env, filename, response, exists[1], self.compute, self.__token
            )
        else:
            response = upload_algo(
                self.env,
                self.project,
                self.org,
                name,
                description,
                self.compute,
                memory,
                "machine",
                algo_type,
                filename,
                self.__token,
            )
            if response.status_code != 201:
                raise Exception(f"Error: {response.status_code} \n{response.text}")
            final_response = finish_algo_upload(
                self.env,
                filename,
                response,
                response.json()["algorithm_id"],
                self.compute,
                self.__token,
            )

        if final_response.status_code != 200:
            raise Exception(
                f"Error: {final_response.status_code} \n{final_response.text}"
            )

        if notification:
            success = get_algo_notification(
                self.env, self.project, self.compute, self.__token
            )
            if not success:
                raise Exception("Algorithm upload error.")
