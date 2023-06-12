import requests
import json
URL = "http://127.0.0.1:8000/emp/"

def get_record(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
        jsondata = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url=URL, headers=headers, data=jsondata)
        data = r.json()
        print(data)
    else:
        jsondata = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        r = requests.get(url=URL, headers=headers, data=jsondata)
        data = r.json()
        print(data)
    
get_record()
get_record(4)