import pytest
import requests
from API.test_api.logger import logger


class BaseService:

    @staticmethod
    def request(method, url, body, code):
        token = getattr(pytest, "token", None)
        if token:
            headers = {"Authorization": f"Bearer {token}"}
        else:
            headers = None
        try:
            response = requests.request(method, url, headers=headers, json=body)
            if code is None:
                response.raise_for_status()
            else:
                assert (
                    response.status_code == code
                ), f"Expected status code {code}, but got {response.status_code}. Response: {response.text}"
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            if response.status_code == 204:
                return None
            if response.text:
                return response.json()
            return None
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None
        except AssertionError as e:
            logger.error("AssertionError. %s", str(e))
            return None

    def delete(self, url, body=None, code=None):
        return self.request("DELETE", url, body, code)

    def post(self, url, token, body=None, code=None):
        return self.request("POST", url, body, code)

    def put(self, url, body=None, code=None):
        return self.request("PUT", url, body, code)

    def get(self, url, code=None):
        return self.request("GET", url, None, code)
