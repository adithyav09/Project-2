import requests
zipapi ="ZVp42kUmPdgG4Na8hYyYEPlhx6cwKcmVZcrDu69nRtPLxcRO92qZFTrkipqJD8dy"
zipcode = "98109"
zipurl = f"https://www.zipcodeapi.com/rest/{zipapi}/info.json/{zipcode}/degrees"

response = requests.get(zipurl).json()
for k in response:
    response[k] = str(response[k])

print(response)
# response
# import http.client

# conn = http.client.HTTPSConnection("api.collectapi.com")

# headers = {
#     'content-type': "application/json",
#     'authorization': "apikey 2NAsuESfcMYcaZ1u3iKmSA:31uTFgKBBkDBiQ0uHgGpID"
#     }

# collecturl = f"/gasPrice/fromCoordinates?lng={response['lng']}&lat={response['lat']}"
# collecturl
from flask import Flask,render_template
from flask_mongoengine import MongoEngine
import json
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'Gasoline',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)
@app.route('/')
def Update ():
    class User(db.Document):
        city = db.StringField()
        state = db.StringField()
        acceptable_city_names=db.StringField()
        timezone =db.StringField()
        zip_code =db.StringField()
        area_codes=db.StringField()
        lng=db.StringField()
        lat=db.StringField()
        # from_json(response, created=False)
    User = User.from_json(json.dumps(response))
    User.save()
    # User.update()
        # print User.to_json()
    return render_template("index.html", Gasoline_data=User)

# User.objects(name="alice").first()
# User(name='laura', email='laura@gmail.com').save()

if __name__ == "__main__":
    app.run(debug=True)
