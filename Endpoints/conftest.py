import pytest
from Endpoints.create_object import CreateObject
from Endpoints.delete_object import DeleteObject



@pytest.fixture()
def id_obj():
    new_object = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object.new_object(payload)

    yield new_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(new_object.response_json['id'])
