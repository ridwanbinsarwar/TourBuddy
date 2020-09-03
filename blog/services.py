""" helper methods for calling api """

import requests
import json
from django.core import serializers


def get_token_from_request(request):
    if request.headers.get('Authorization') is None:
        # request from browser
        try:
            token = request.session['token']
            token = 'Bearer ' + token
        except KeyError:
            # user not authorized
            return "unauthorized"
    else:
        # request from Postman
        token = request.headers.get('Authorization')
    return token


def get_post_by_user(token, user):
    url = 'http://127.0.0.1:8000/api/article/'
    headers = {'Authorization': token}
    jsn = {'user': user}
    r = requests.get(url, json=jsn, headers=headers)
    posts = r.json()
    return posts


def upload_post(obj, token):
    url = 'http://127.0.0.1:8000/api/article/'
    # converting obj to query obj and serialize
    data = json.loads(serializers.serialize('json', [obj]))[0]
    data = json.dumps(data)
    # converting string to json
    json_obj = json.loads(data)
    headers = {'Authorization': token}

    r = requests.post(url=url, json=json_obj["fields"], headers=headers)
    print(type(r.json()))
    return r


def view_post_api(id):
    url = 'http://127.0.0.1:8000/api/detail/%s' % id
    response = requests.get(url)
    post = response.json()
    return post


def delete_post_api(id, token):
    url = 'http://127.0.0.1:8000/api/detail/%s' % id
    headers = {'Authorization': token}
    response = requests.delete(url=url, headers=headers)
    return response


def update_post_api(post, id, token):
    url = 'http://127.0.0.1:8000/api/detail/%s/' % id
    # converting obj to query obj and serialize
    data = json.loads(serializers.serialize('json', [post]))[0]
    data = json.dumps(data)
    # converting string to json
    json_obj = json.loads(data)
    headers = {'Authorization': token}
    r = requests.put(url=url, json=json_obj["fields"], headers=headers)
    return r



