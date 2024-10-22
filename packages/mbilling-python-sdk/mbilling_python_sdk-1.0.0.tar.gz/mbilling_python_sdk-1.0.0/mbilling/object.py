class MagnusBillingObject:
    def __init__(self, resource, data):
        self.resource = resource
        self.data = data

    def update(self, **kwargs):
        updated_data = self.resource.update(self.data["id"], kwargs)
        if updated_data:
            self.data.update(updated_data)
        return self

    def __getattr__(self, item):
        return self.data.get(item)

    def __repr__(self):
        return f"{self.data}"
