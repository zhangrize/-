import requests
from config.config import BASE_URL

def api_get(endpoint, params=None, headers=None):
    url = f"{BASE_URL}/{endpoint}"
    return requests.get(url, params=params, headers=headers)

def api_post(endpoint, json_data=None, headers=None):
    url = f"{BASE_URL}/{endpoint}"
    return requests.post(url, json=json_data, headers=headers)
