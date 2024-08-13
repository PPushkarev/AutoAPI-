import requests
from Endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):
    def get_by_id(self, id_obj):
        self.response = requests.get(f"https://api.restful-api.dev/objects/{id_obj}")
        self.response_json = self.response.json()

    def check_response_id(self, id_obj):
        assert self.response_json['id'] == id_obj
