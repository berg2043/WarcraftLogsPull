import requests
import json
import numpy as np
import pandas as pd

""" This program currently pulls  the top 100 dps for each boss in Uldir.  It can be changed
to pull the top 100 dps for any raid on any difficulty.  These are combined into a single xlsx file. """

# User inputs
apikey = '<API KEY HERE>' #api key in ''  
raid = 'Uldir' # raid name in ''
dificulty = 5 # 1 = LFR, 2 = Flex, 3 = Normal, 4 = Heroic, 5 = Mythic, 10 = Challenge Mode

# defaults for DPS
url = 'https://www.warcraftlogs.com:443/v1/'
call = 'rankings/encounter/'
id = '2144'
metric = '?metric=dps'
dif = '&difficulty=' + str(dificulty)
region = '&region=US'
pnumb = 1
page = '&page=' + str(pnumb)
zoneurl = 'https://www.warcraftlogs.com/v1/zones?api_key='
classurl = 'https://www.warcraftlogs.com/v1/classes?api_key='

# initial data pulls
zoner = requests.get(zoneurl + apikey)
zone = zoner.json()
classesr = requests.get(classurl + apikey)
classes = classesr.json()
#r = requests.get(url + call + str(q['id']) + metric + dif + region + page + '&api_key=' + apikey)

# Takes the data and places it. Also changes the value for classes and specs to their names
def organize(datas, name, excel):
  df = pd.DataFrame(columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])
  for parse in datas:
    list =[]
    list.append(parse['name'])
    for cl in classes:
      if cl['id'] == parse['class']:
        list.append(cl['name'])
        for sp in cl['specs']:
          if sp['id'] == parse['spec']:
            list.append(sp['name'])
    list.append(parse['itemLevel'])
    list.append(parse['total'])
    df2 = pd.DataFrame([list], columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])
    df = df.append(df2, ignore_index=True)
  df.to_excel(excel, name, index=False)

# main function that pulls for each boss and saves the xlsx file
def puller():
  writer = pd.ExcelWriter(raid + '.xlsx')
  for tier in zone:
    if tier['name'] == raid:
      for boss in tier['encounters']:
        r = requests.get(url + call + str(boss['id']) + metric + dif + region + page + '&api_key=' + apikey)
        pull = r.json()
        organize(pull['rankings'], boss['name'], writer)
  writer.save()

puller()
