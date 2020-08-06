""" helper methods for calling api """

import requests
import json
from django.core import serializers


def get_profile_api(token):
    url = 'http://127.0.0.1:8000/api/profile/'
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    return response.json()


def update_profile_api(json_data, token):
    url = 'http://127.0.0.1:8000/api/profile/'
    headers = {'Authorization': token}

    response = requests.put(url, headers=headers, json=json_data)
    return response.json()


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
