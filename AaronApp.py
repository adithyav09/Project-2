import requests
import http.client
from flask import Flask, render_template,redirect,request
import sqlite3
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from statefips import States_fipsId

# def get_db_connection():
#     conn = sqlite3.connect('gasdatabase.db')
#     conn.row_factory = sqlite3.Row
#     return conn

###Testing database  SQL queries in terminal
# conn = get_db_connection()
# curs = conn.cursor()
# currentprices = curs.execute("""SELECT * FROM hist_gas_prices WHERE Date LIKE 2020""")
# for row in currentprices:
#     print(*row)
# conn.close()

##Query some region stuff?
# def getregion():
#     conn = get_db_connection()
#     chosenregion = conn.execute('SELECT (Date,' + regioninput + '') FROM hist_gas_prices WHERE ')



# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        zipcode = "31402"
        zipapi = "5kF2PxrgxTE9vrkZuSAchlb4SVaKrJgW5ewTfqiucVyZfcyaqLfN9JmRt98YNuol"
        zipurl = f"https://www.zipcodeapi.com/rest/{zipapi}/info.json/{zipcode}/degrees"
        response = requests.get(zipurl).json()
        
        conn = http.client.HTTPSConnection("api.collectapi.com")
        
        headers = {
        'content-type': "application/json",
        'authorization': "apikey 60NpjP2khNX0u5YCngWVa8:3q7xw9Ij4XoszUMayKd6lk"
        }

        collecturl = f"/gasPrice/fromCoordinates?lng={response['lng']}&lat={response['lat']}"
        conn.request("GET",collecturl,headers=headers)
        res = conn.getresponse()
        data = res.read()
        Gdata = json.loads(data)
        print(Gdata)
        Gdata = Gdata['result']
        return render_template("index.html", Gasoline_data=Gdata) 
    else:
        zipcode = request.form['zipcode']
        zipapi = "ZVp42kUmPdgG4Na8hYyYEPlhx6cwKcmVZcrDu69nRtPLxcRO92qZFTrkipqJD8dy"
        zipurl = f"https://www.zipcodeapi.com/rest/{zipapi}/info.json/{zipcode}/degrees"
        response = requests.get(zipurl).json()
        
        conn = http.client.HTTPSConnection("api.collectapi.com")
        
        headers = {
        'content-type': "application/json",
        'authorization': "apikey 60NpjP2khNX0u5YCngWVa8:3q7xw9Ij4XoszUMayKd6lk"
        }

        collecturl = f"/gasPrice/fromCoordinates?lng={response['lng']}&lat={response['lat']}"
        conn.request("GET",collecturl,headers=headers)
        res = conn.getresponse()
        data = res.read()
        Gdata = json.loads(data)
        print(Gdata)
        Gdata = Gdata['result']
        
        return render_template("index.html", Gasoline_data=Gdata)


@app.route("/Charts")
def choropleth():
    return render_template('charts.html')

@app.route("/News")
def addNews():
    return render_template('News.html')

@app.route("/Years")
def Years():
    Base = automap_base()
    engine = create_engine('sqlite:///gasdatabase.db')
    Base.prepare(engine, reflect = True)
    HistGasPrices = Base.classes.hist_gas_prices
    session = Session(engine)
    histgasprices = session.query(HistGasPrices)
    
    return render_template('Years.html', histgasprices=histgasprices)

# @app.route("/Years")
# def Years():
#     conn = get_db_connection()
#     currentprices = conn.execute('SELECT * FROM hist_gas_prices WHERE Date LIKE 2020*').fetchall()
#     histprices = conn.execute('SELECT * FROM hist_gas_prices WHERE Date LIKE ' + yearinput + '*').fetchall()
#     conn.close()
#     yearinput = request.form['text']
#     return render_template('Years.html')


if __name__ == "__main__":
    app.run(debug=True)










