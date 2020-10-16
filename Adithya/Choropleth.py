#!/usr/bin/env python
# coding: utf-8

# In[67]:


#Import Dependencies
import requests
import http.client
import json
import geojson
import time


# In[1]:


#Fetch the data using API and client format
import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 095qy5emUONDSAcb8TZFvG:0lLiUg1Hj1hxHS9mCEob3m"
    }

conn.request("GET", "/gasPrice/allUsaPrice", headers=headers)

res = conn.getresponse()
raw_data = res.read()

#Printing the results after decoding from bytes to review data
print(raw_data.decode("utf-8"))


# In[303]:


#Converting the byte array by decoding and then loading through JSON
gasPriceState_data = raw_data.decode('utf8')
gasPriceState_data = json.loads(gasPriceState_data)
gasPriceState_data = gasPriceState_data['result']
print(gasPriceState_data)


# In[372]:


#Recieved fips ID for each state in order to change apply it into the gasPrice JSON dictionary by matching by state key
States_fipsId = {
'Alabama': '01',
'Alaska': '02',
'Arizona': '04',
'Arkansas': '05',
'California': '06',
'Colorado': '08',
'Connecticut': '09',
'Delaware': '10',
'District Of Columbia': '11',
'Florida': '12',
'Georgia': '13',
'Hawaii': '15',
'Idaho': '16',
'Illinois': '17',
'Indiana': '18',
'Iowa': '19',
'Kansas': '20',
'Kentucky': '21',
'Louisiana': '22',
'Maine': '23',
'Maryland': '24',
'Massachusetts': '25',
'Michigan': '26',
'Minnesota': '27',
'Mississippi': '28',
'Missouri': '29',
'Montana': '30',
'Nebraska': '31',
'Nevada': '32',
'New Hampshire': '33',
'New Jersey': '34',
'New Mexico': '35',
'New York': '36',
'North Carolina': '37',
'North Dakota': '38',
'Ohio': '39',
'Oklahoma': '40',
'Oregon': '41',
'Pennsylvania': '42',
'Rhode Island': '44',
'South Carolina': '45',
'South Dakota': '46',
'Tennessee': '47',
'Texas': '48',
'Utah': '49',
'Vermont': '50',
'Virginia': '51',
'Washington': '53',
'West Virginia': '54',
'Wisconsin': '55',
'Wyoming': '56'
}


# In[379]:


# #Testing to see if the id state works
gasPriceState_data = sorted(gasPriceState_data, key = lambda i: i['name'])
    
for gasDict, state_id in zip(gasPriceState_data, States_fipsId.values()):
    gasDict['id'] = state_id
    print(gasDict)

with open('static/data/gasPriceState.json', 'w') as fp:
    json.dump(gasPriceState_data, fp)


# In[ ]:


# geojson = {
#     "type": "FeatureCollection",
#     "features": [
#     {
#       "type": "Feature", "id":"(ID NUMBER)", "properties" : {"name":(STATE), "gasolineData": (GAS DATA), "midGradeData":(MID DATA), "premiumData": (PREM DATA),"dieselData": (DIESEL DATA)},
#         "geometry" : {
#             "type": "Polygon",
#             "coordinates": [d["lon"], d["lat"]],
#             },
#      } for d in stateData]
# }


# In[ ]:


# with open("static/data/statesData.geojson") as f:
#     gj = geojson.load(f)
#     print(gj)

