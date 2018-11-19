import json
import numpy as np
import pandas as pd

with open('data2.json') as file:
  data = json.load(file)

df = pd.DataFrame(columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])
  
def pull(x):
  for n in x:
    global df
    list =[]
    list.append(n['name'])
    list.append(n['class'])
    list.append(n['spec'])
    list.append(n['itemLevel'])
    list.append(n['total'])
    df2 = pd.DataFrame([list], columns = ['Name', 'Class', 'Spec', 'ilvl', 'dps'])
    df = df.append(df2, ignore_index=True)

pull(data['rankings'])
print(df)
