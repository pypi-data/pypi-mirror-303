import json
import random
import requests
from typing import Text, Dict
from requests import Response

from ipakyuli.exception import AuthenticationFailed, AuthRevokeTokenFailed


class BankIntegration:
    def __init__(self, api_url: Text, login: Text, password: Text, cash_box_id: Text):
        self.__api_url: Text = api_url
        self.__login: Text = login
        self.__password: Text = password
        self.__cash_box_id: Text = cash_box_id

        self.__auth_token: Text = ""
        self.request_id: Text = str(random.randint(1000, 99999))
        self.__headers: Dict = {
            "Content-Type": "application/json",
        }

        self.auth_get_token()

    def post(self, url: Text, data: Dict) -> Response:
        """Use this method to send request"""
        data["id"] = self.request_id

        response = requests.post(
            url=self.__api_url + url, data=json.dumps(data), headers=self.__headers
        )
        response.raise_for_status()  # Raise exception for non-2xx responses
        return response

    def auth_get_token(self):
        data = {
            "jsonrpc": "2.0",
            "method": "auth.get_token",
            "params": {
                "login": self.__login,
                "password": self.__password,
                "cashbox_id": self.__cash_box_id,  # noqa
            },
        }

        response = self.post(url="/auth", data=data)

        if response.status_code == 201:
            response_json = response.json()
            self.__auth_token = response_json.get("result", {}).get("token")
            self.__headers["Authorization"] = f"Bearer {self.__auth_token}"

        else:
            raise AuthenticationFailed()

    def auth_token_revoke(self):
        data = {
            "jsonrpc": "2.0",
            "method": "auth.token_revoke",
            "params": {
                "login": self.__login,
                "password": self.__password,
                "token": self.__auth_token,
            },
        }

        response = self.post(url="/auth", data=data).json()

        if response.get("result", {}).get("message") != "Token revoked successfully":
            raise AuthRevokeTokenFailed()
