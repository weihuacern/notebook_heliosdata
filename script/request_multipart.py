import json

import requests

API_PROXY = "http://192.168.7.140:8000"
API_URL = "/api/v1/datasource/forms/"

if __name__ == "__main__":
    r = requests.post(API_PROXY + API_URL, files=dict(foo='bar'))
    r_dict = json.loads(r.text)
    print(r_dict)
