import json
import numpy as np
import pandas as pd

# opens JSONs for data, class and zones
with open('data2.json') as file:
  data = json.load(file)
with open('class.json') as file:
  classes = json.load(file)
#with open('zone.json') as file:
#  zone = json.load(file)

# Creates DataFrame for data to be organized in
df = pd.DataFrame(columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])

# Pulls the data and places it. Also changes the value for classes and specs to their names
def organize(datas):
  for parse in datas:
    global df
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

# won't work for JSONs but will work to create multiple URL strings to pull from
#for n in zone:
#  if n['name'] == raid:
#    for q in n['encounters']:
      #print(q['name'])
      # (url + call + str(q['id']) + metric + dif + region + page + '&api_key=' + apikey + '\n')
      #print(q['id'])

organize(data['rankings'])
print(df)
