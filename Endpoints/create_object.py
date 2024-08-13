import requests
from Endpoints.base_endpoint import Endpoint

payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }


class CreateObject(Endpoint):
    def new_object(self, payload):
        self.response = requests.post("https://api.restful-api.dev/objects", json=payload)
        self.response_json = self.response.json()
        id_obj = self.response_json['id']
        return id_obj


    def check_name(self, name):
        assert self.response_json['name'] == payload['name']
