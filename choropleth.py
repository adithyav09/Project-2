#Import Dependencies
import requests
import http.client
import json
from statefips import States_fipsId
import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 095qy5emUONDSAcb8TZFvG:0lLiUg1Hj1hxHS9mCEob3m"
    }

conn.request("GET", "/gasPrice/allUsaPrice", headers=headers)

res = conn.getresponse()
raw_data = res.read()

print(raw_data.decode("utf-8"))
print(States_fipsId)

#Converting the byte array by decoding and then loading through JSON
gasPriceState_data = raw_data.decode('utf8')
gasPriceState_data = json.loads(gasPriceState_data)
gasPriceState_data = gasPriceState_data['result']
print(gasPriceState_data)

# #Testing to see if the id state works
gasPriceState_data = sorted(gasPriceState_data, key = lambda i: i['name'])
    
for gasDict, state_id in zip(gasPriceState_data, States_fipsId.values()):
    gasDict['id'] = state_id
    print(gasDict)

# with open('static/data/gasPriceState.json', 'w') as fp:
#     json.dump(gasPriceState_data, fp)






