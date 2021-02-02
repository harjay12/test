import requests
import os
from api_key import API_KEY

def add_func(x,y):
    return x + y



KEY = API_KEY

# envkey=os.environ.get("API_KEY")

URL = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?'

def accessingapi(url):
    res = requests.get(url, params={'api_key': KEY})
    return res

print(accessingapi(URL))
#t='ERWA'
# print(func(t))

# def test_fact():
#     assert (func(t))

