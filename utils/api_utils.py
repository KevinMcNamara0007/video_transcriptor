import requests

def fetch_data(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def post_data(url, data, headers=None):
    response = requests.post(url, json=data, headers=headers)
    return response.json()

