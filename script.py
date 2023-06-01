import requests
import pprint 
#import json
from matplotlib import pyplot as plt
from datetime import datetime

API_URL = "https://rickandmortyapi.com/api/episode"
r = requests.get(API_URL)
resp = r.json()
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(resp)

episodes = {}
for res in resp['results']:
    episodes[res["name"]] = len(res["characters"])

pp.pprint(episodes)


#json dumps way 
#episodes = {}
#for res in resp['results]:
    #episodes[res["name"]] = len(res["characters"])
#print(json.dumps(episode, indent=4))

plt.xlabel('episode name')
plt.xticks(rotation=90)
plt.ylabel('character count')
plt.plot(episodes.keys(), episodes.values())
plt.show()