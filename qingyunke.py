import requests
import json

url = 'http://api.qingyunke.com/api.php'

def chat(msg):
    params = {'key': 'free',
              'appid': '0',
              'msg': msg}
    r = requests.get(url=url, params=params)
    j = json.loads(r.text)
    return j["content"]