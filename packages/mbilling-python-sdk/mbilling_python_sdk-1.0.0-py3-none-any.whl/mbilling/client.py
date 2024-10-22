import hashlib
import hmac
import logging
import time

from urllib.parse import urlencode, urljoin

import requests

from mbilling.resource import MagnusBillingResource


class MagnusBilling:
    def __init__(self, api_key, api_secret, public_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.public_url = public_url

        self.users = MagnusBillingResource(self, "user")

    def query(self, request):
        module = request.get("module")
        action = request.get("action")

        # generate nonce
        request["nonce"] = self.create_nonce()

        post_data = self.generate_query_string(request)
        sign = self.generate_sign(post_data)

        headers = {"Content-Type": "application/x-www-form-urlencoded", "Key": self.api_key, "Sign": sign}
        url = urljoin(self.public_url, f"index.php/{module}/{action}")

        try:
            response = requests.post(url, data=post_data, headers=headers, verify=False)
            response.raise_for_status()
        except requests.RequestException as error:
            logging.error("Caught an error trying to make request.")
            logging.error("Request URL: %s\nRequest Error: %s" % (url, error))
            raise

        return response.json()

    @staticmethod
    def create_nonce():
        return str(int(time.time() * 1000))

    @staticmethod
    def generate_query_string(params):
        return urlencode(params)

    def generate_sign(self, post_data):
        return hmac.new(self.api_secret.encode(), post_data.encode(), hashlib.sha512).hexdigest()
