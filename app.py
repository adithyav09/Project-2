import requests
zipapi ="ZVp42kUmPdgG4Na8hYyYEPlhx6cwKcmVZcrDu69nRtPLxcRO92qZFTrkipqJD8dy"
zipcode = "31405"
zipurl = f"https://www.zipcodeapi.com/rest/{zipapi}/info.json/{zipcode}/degrees"

response = requests.get(zipurl).json()
# for k in response:
#     response[k] = str(response[k])

print(response)
# response
import http.client



# from flask import Flask,render_template
# from flask_mongoengine import MongoEngine
# import json
# app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'Gasoline',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)
# @app.route('/')
# def Update ():
#     class User(db.Document):
#         city = db.StringField()
#         state = db.StringField()
#         acceptable_city_names=db.StringField()
#         timezone =db.StringField()
#         zip_code =db.StringField()
#         area_codes=db.StringField()
#         lng=db.StringField()
#         lat=db.StringField()
#         # from_json(response, created=False)
#     User = User.from_json(json.dumps(response))
#     User.save()
#     # User.update()
#         # print User.to_json()
#     return render_template("index.html", Gasoline_data=User)

# User.objects(name="alice").first()
# User(name='laura', email='laura@gmail.com').save()

# if __name__ == "__main__":
#     app.run(debug=True)

# import necessary libraries
from flask import Flask, render_template,redirect
#import scrape_mars
import pymongo
import json
# import scrape_mars



# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.Gas_Data
collection = db.State_Data



# create instance of Flask app
app = Flask(__name__)



# create route that renders index.html template
@app.route("/")
def index():
    data = list(collection.find())
    print(type(data[-1]))
    print(data[-1])
    return render_template("index.html", Gasoline_data=data[-1])
     

#create route that does the scrape and stored the returned value in Mongodb    
@app.route("/update")
def Update():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    
    headers = {
    'content-type': "application/json",
    'authorization': "apikey 2NAsuESfcMYcaZ1u3iKmSA:31uTFgKBBkDBiQ0uHgGpID"
    }

    collecturl = f"/gasPrice/fromCoordinates?lng={response['lng']}&lat={response['lat']}"
    conn.request("GET",collecturl,headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    data = json.loads(data)
    data = data['result']
    print(data)
    # print(data.decode("utf-8"))

    # collection.insert_one(data)
    collection.update({},data,upsert=True)
 
    return redirect("/",code=302)

@app.route("/Charts")
def addnew():
    return render_template('charts.html')

@app.route("/News")
def addNews():
    return render_template('News.html')

@app.route("/About")
def About():
    return render_template('About.html')
    

   
if __name__ == "__main__":
    app.run(debug=True)










