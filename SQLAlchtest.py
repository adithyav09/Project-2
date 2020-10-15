# from flask import Flask, render_template,redirect,request
# from datetime import date
# from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


Base = automap_base()
engine = create_engine('sqlite:///gasdatabase.db')

Base.prepare(engine, reflect = True)

HistGasPrices = Base.classes.hist_gas_prices

session = Session(engine)
histgasprices = session.query(HistGasPrices)

for price in histgasprices:
    print (price.Date, price.New_England_Prices)
    
data = "2008*"
Gprice2008 = histgasprices.filter(HistGasPrices.Date.like(data)).all()

for g in Gprice2008:
    print(g)