import requests
import pprint 
from matplotlib import pyplot as plit
from datetime import datetime

API_URL = "https://rickandmortyapi.com/api/character/?status=alive"
r = requests.get(API_URL)
resp = r.json()
print(resp)