import requests
import os

def add_func(x,y):
    return x + y



envkey=os.environ.get("API_KEY")
URL = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?'

def accessingapi(url):
    res = requests.get(url, params={'api_key': envkey})
    return res

print(accessingapi(URL))
#t='ERWA'
# print(func(t))

# def test_fact():
#     assert (func(t))

