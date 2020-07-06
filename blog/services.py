import requests


def get_all_post():
    url = 'http://127.0.0.1:8000/api/article/'
    r = requests.get(url)
    books = r.json()
    return books

