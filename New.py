import requests
import http.client
# import necessary libraries
from flask import Flask, render_template,redirect,request
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

def call_api(zip_code):
    if zip_code is None:
        zip_code = "98109"
    zipapi ="ZVp42kUmPdgG4Na8hYyYEPlhx6cwKcmVZcrDu69nRtPLxcRO92qZFTrkipqJD8dy"
    zipcode = zip_code
    zipurl = f"https://www.zipcodeapi.com/rest/{zipapi}/info.json/{zipcode}/degrees"
    response = requests.get(zipurl).json()
    return response

def update_db(response):
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

# create route that renders index.html template
@app.route("/")
def index():
    data = call_api("98109")
    update_db(data)
    data = list(collection.find())
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
    
@app.route("/zipcode", methods=["POST"])
def zip():
    zipcode = request.form['zipcode']
    print(zipcode)
    data = call_api(zipcode)
    update_db(data)
    data = list(collection.find())
    return render_template("index.html", Gasoline_data=data[-1])
   
if __name__ == "__main__":
    app.run(debug=True)










