import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('gasdatabase.db')
    conn.row_factory = sqlite3.Row
    return conn


###Testing database  SQL queries in terminal
conn = get_db_connection()
curs = conn.cursor()
currentprices = curs.execute("""SELECT * FROM hist_gas_prices WHERE Date LIKE 2020%""")
for row in currentprices:
    print(*row, sep='\t')
conn.close()


##Query some region stuff?
# def getregion():
#     conn = get_db_connection()
#     chosenregion = conn.execute('SELECT (Date,' + regioninput + '') FROM hist_gas_prices WHERE ')

###Intialize flask
# app = Flask(__name__)

###Open html with a database connection
# @app.route('/')
# def index():
#     conn = get_db_connection()
#     currentprices = conn.execute('SELECT * FROM hist_gas_prices WHERE Date LIKE 2020*').fetchall()
#     conn.close()
#     return render_template('index.html')

##Get User Input for Year and give it to Flask
# @app.route('/', methods=['POST'])
# def priceyearpost():
#    yearinput = request.form['text']
#    return yearinput

###Use User input to Query
# def year_input_data(yearinput):
#     conn = get_db_connection()
#      histprices = conn.execute('SELECT * FROM hist_gas_prices WHERE Date LIKE ' + yearinput + '*').fetchall()
#      conn.close()
#      if histprices is None:
#          histprices = 0
#      return histprices

