import requests
import json

apikey = '&api_key=<API KEY HERE>'
url = 'https://www.warcraftlogs.com:443/v1/'
call = 'rankings/encounter/'
id = '2144'
metric = '?metric=dps'
dif = '&difficulty=4'
region = '&region=US'
numb = 1
page = '&page=' + str(numb)

r = requests.get(url + call + id + metric + dif + region + page + apikey)
thing = r.json()

def pull(x):
  for n in x:
    print(n['name'])
    print(n['total'])

pull((thing['rankings']))
