import requests
import json
from django.core import serializers


def get_all_post():
    url = 'http://127.0.0.1:8000/api/article/'
    r = requests.get(url)
    books = r.json()
    return books


def upload_post(obj):
    url = 'http://127.0.0.1:8000/api/article/'
    # converting obj to query obj and serialize
    data = json.loads(serializers.serialize('json', [obj]))[0]
    data = json.dumps(data)
    # converting string to json
    json_obj = json.loads(data)

    requests.post(url=url, json=json_obj["fields"])
