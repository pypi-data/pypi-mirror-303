import json
from typing import List

from mbilling import MagnusBillingObject


class MagnusBillingResource:
    def __init__(self, client, resource_name: str):
        self.client = client
        self.resource_name = resource_name

    def list(self, action="read", page=1):
        response = self.client.query({"module": self.resource_name, "action": action, "page": page})

        if response and "rows" in response:
            return [MagnusBillingObject(self, row) for row in response["rows"]]

        return []

    def get(self, action="read", **kwargs):
        field, value = next(iter(kwargs.items()))

        request = {
            "module": self.resource_name,
            "action": action,
            "filter": json.dumps([{"type": "string", "field": field, "value": value, "comparison": "eq"}]),
        }

        response = self.client.query(request)

        if response and "rows" in response and response["rows"]:
            return MagnusBillingObject(self, response["rows"][0])

        return None

    def update(self, resource_id, data, action="save"):
        request = {"module": self.resource_name, "action": action, "id": resource_id, **data}

        response = self.client.query(request)

        if response and "rows" in response:
            return response["rows"][0]

        return None
