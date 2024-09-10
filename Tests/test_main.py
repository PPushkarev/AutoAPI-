# Testing of API https://restful-api.dev/ Get, Put, Delete,
# set PYTHONPATH=C:\Users\User\PycharmProjects\pythonProject5\Endpoints
import pytest

from Endpoints.conftest import id_obj
from Endpoints.create_object import CreateObject
from Endpoints.get_object import GetObject
from Endpoints.update_object import UpdateObject
from Endpoints.delete_object import DeleteObject
import allure

#


@allure.title('Test creation object')
def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(payload['name'])
    new_object_endpoint.status_code()

@allure.title('Test GET')
def test_get_object(id_obj):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(id_obj)
    get_object_endpoint.check_response_id(id_obj)
    get_object_endpoint.status_code()

@allure.title('Test PUT')
def test_put_object(id_obj):
    update_object_endpoint = UpdateObject()
    payload = {
        "name": "Apple MacBook Pro 1446",
        "data": {
            "year": 204419,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    update_object_endpoint.update_by_id(id_obj, payload)
    update_object_endpoint.status_code()
    update_object_endpoint.check_response_name(payload['name'])

@allure.title('Test DELETE')
def test_delete_object(id_obj):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(id_obj)
    delete_object_endpoint.status_code()
