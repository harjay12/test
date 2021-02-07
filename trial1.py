import requests
import os
# from api_key import API_KEY
from dotenv import load_dotenv


def add_func(x, y):
    return x + y


load_dotenv()
key = os.getenv("API_KEY")
# KEY = API_KEY

# envkey=os.environ.get("API_KEY")

URL = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?'


def accessingapi(url):
    res = requests.get(url, params={'api_key': key})
    return res


print(accessingapi(URL))


# t='ERWA'
# print(func(t))

# def test_fact():
#     assert (func(t))
