import requests
from Endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):

    def delete_by_id(self, id_obj):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{id_obj}")
        self.response_json = self.response.json()
