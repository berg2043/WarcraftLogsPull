import requests
import json
import numpy as np
import pandas as pd

""" This program currently pulls all dps rankings for each boss in Uldir.  It can be changed
to pull the all dps rankings for any raid on any difficulty.  These are put into individual CSV files.
Future versions will organize them into an xlsx file for analysis. """

# User inputs
apikey = '<API KEY HERE>' #api key in ''  
raid = 'Uldir' # raid name in ''
dificulty = 5 # 1 = LFR, 2 = Flex, 3 = Normal, 4 = Heroic, 5 = Mythic, 10 = Challenge Mode

# defaults for DPS
url = 'https://www.warcraftlogs.com:443/v1/'
call = 'rankings/encounter/'
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

# Takes the data and places it. Also changes the value for classes and specs to their names
def organize(datas, frame):
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
    frame = frame.append(df2, ignore_index=True)
  return(frame)

#this is the machine that runs through all the rankings not just the top 100
def full(boss):
  check = True
  pagen = 1
  pages = '&page=' + str(pagen)
  df = pd.DataFrame(columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])
  while check == True:
    r = requests.get(url + call + str(boss['id']) + metric + dif + region + pages + '&api_key=' + apikey)
    pull = r.json()
    df = organize(pull['rankings'], df)
    pagen += 1
    pages = '&page=' + str(pagen)
    check = pull['hasMorePages']
  df.to_csv(boss['name'] + '_Full.csv', index = False)

# main function that pulls for each boss and makes a CSV using organize's dataframe
def puller():
  for tier in zone:
    if tier['name'] == raid:
      for bosses in tier['encounters']:
        full(bosses)

puller()
