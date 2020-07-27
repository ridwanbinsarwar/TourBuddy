""" helper methods for calling api """

import requests
import json
from django.core import serializers


def register_user_api(data):
    url = 'http://127.0.0.1:8000/api/account/register/'
    # CONVERT DATA TO A STRING OF A JSON OBJECT
    json_dump = json.dumps(data)
    # creating json object
    json_obj = json.loads(json_dump)
    return requests.post(url=url, json=json_obj)


def login_user_api(data):
    url = 'http://127.0.0.1:8000/api/account/login/'
    # CONVERT DATA TO A STRING OF A JSON OBJECT
    json_dump = json.dumps(data)
    # creating json object
    json_obj = json.loads(json_dump)
    return requests.post(url=url, json=json_obj)
