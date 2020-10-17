import requests
import http.client
from flask import Flask, render_template,redirect,request
import sqlite3
import json
from sqlalchemy import create_engine, extract
from sqlalchemy.orm import Session
from init_db import HistGasPrices





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
        Gdata = Gdata['result']
        
        return render_template("index.html", Gasoline_data=Gdata)


@app.route("/Charts")
def addnew():
    return render_template('charts.html')

@app.route("/News")
def addNews():
    return render_template('News.html')


@app.route("/Years", methods=["GET","POST"])
def Years():
    engine = create_engine('sqlite:///gasdatabase.db')
    session = Session(engine)
    histgasprices = session.query(HistGasPrices)


    if request.method == "GET":
        currentyearprices = "2020"
        Query = histgasprices.filter(HistGasPrices.Year == currentyearprices)   
        for r in Query:
            Years = [r.Year for r in Query]
            Dates = [r.Date for r in Query]
            NEPrices = [r.New_England_Prices for r in Query]
            CAPrices = [r.Central_Atlantic_Prices for r in Query]
            LAPrices = [r.Lower_Atlantic_Prices for r in Query]
            MWPrices = [r.Midwest_Prices for r in Query]
            GFPrices = [r.Gulf_Coast_Prices for r in Query]
            RMPrices = [r.Rocky_Mountain_Prices for r in Query]
            WCPrices = [r.West_Coast_Prices for r in Query]
            NoCAPrices = [r.West_Coast_No_Cali_Prices for r in Query]
            
        HistoricalData = {"Dates":Dates, "NEPrices":NEPrices, "CAPrices":CAPrices, "LAPrices":LAPrices,"MWPrices":MWPrices, "GFPrices":GFPrices, "RMPrices":RMPrices, "WCPrices":WCPrices, "NoCAPrices":NoCAPrices }
        return render_template('Years.html', HistoricalData=HistoricalData)
    
    else: 
        useryear = request.form['useryear']
        Query = histgasprices.filter(HistGasPrices.Year == useryear)
        for r in Query:
            Years = [r.Year for r in Query]
            Dates = [r.Date for r in Query]
            NEPrices = [r.New_England_Prices for r in Query]
            CAPrices = [r.Central_Atlantic_Prices for r in Query]
            LAPrices = [r.Lower_Atlantic_Prices for r in Query]
            MWPrices = [r.Midwest_Prices for r in Query]
            GFPrices = [r.Gulf_Coast_Prices for r in Query]
            RMPrices = [r.Rocky_Mountain_Prices for r in Query]
            WCPrices = [r.West_Coast_Prices for r in Query]
            NoCAPrices = [r.West_Coast_No_Cali_Prices for r in Query]
            
        HistoricalData = {"Dates":Dates, "NEPrices":NEPrices, "CAPrices":CAPrices, "LAPrices":LAPrices,"MWPrices":MWPrices, "GFPrices":GFPrices, "RMPrices":RMPrices, "WCPrices":WCPrices, "NoCAPrices":NoCAPrices }
        
        return render_template('Years.html', HistoricalData=HistoricalData)




if __name__ == "__main__":
    app.run(debug=True)








