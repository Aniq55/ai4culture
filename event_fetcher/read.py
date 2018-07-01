import pandas as pd
import numpy as np
from nltk.corpus import stopwords, wordnet
import re
import requests
import json


user_key = "pQdnG7QPbTD2KhZh"

df= pd.read_csv("events.csv")

# l1= len(df)

df= df.drop_duplicates('id')

# headers = list(df.columns.values)

notnull_headers = ['latitude','longitude','id', 'title', 'city_name']

for header in notnull_headers:
    df = df[df[header].notnull()]

# l2= len(df)

# print(l1-l2)
# print(df)

SIZE = len(df)

# stop_words = stopwords.words('english')
# stop_words.extend(stopwords.words('french'))
#
# LIST= []
# for v in df['description']:
#     # des = str(v).split()
#     des= re.split(' |; |, |\*|\n', v)
#     x = [d for d in des if not d in stop_words]
#     LIST.append(x)
#
# df['description'] = LIST

# print(df['description'])


req_features= ['address', 'price', 'description', 'venue_type', 'performers', 'title', 'id', 'tags', 'categories' ]
for v in df['id']:
    data = requests.get('http://api.eventful.com/json/events/get?&id='+ v+ "&app_key=" + user_key).json()
    # print(data)
    # for i in range(len(data)):
        # print(data["categories"]['id'])
    for feature in req_features:
        y = data[feature]
        print(y)
        print("==================")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")

for x in df['description']:
    print(x)
    print("============================")
print(len(df))