""" helper methods for calling api """

import requests
import json
from django.core import serializers


def get_all_post():
    url = 'http://127.0.0.1:8000/api/article/'
    r = requests.get(url)
    posts = r.json()
    return posts


def upload_post(obj):
    url = 'http://127.0.0.1:8000/api/article/'
    # converting obj to query obj and serialize
    data = json.loads(serializers.serialize('json', [obj]))[0]
    data = json.dumps(data)
    # converting string to json
    json_obj = json.loads(data)

    requests.post(url=url, json=json_obj["fields"])


def view_post_api(id):
    url = 'http://127.0.0.1:8000/api/detail/%s' % id
    response = requests.get(url)
    post = response.json()
    return post


def delete_post_api(id):
    url = 'http://127.0.0.1:8000/api/detail/%s' % id
    response = requests.delete(url)
    return response
