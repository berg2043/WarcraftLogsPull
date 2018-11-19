import requests
import json

apikey = '&api_key=81e7e6e4402a160beb16a24e735d62b4'
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
with f = open('data.json','w') as outfile:
  json.dump(data, outfile)

#def pull(x):
#  for n in x:
#    print(n['name'])
#    print(n['total'])

#pull((thing['rankings']))
