import sqlite3
import pandas as pd


conn = sqlite3.connect('gasdatabase.db')

with open('SQLSchema.sql') as schfile:
    conn.executescript(schfile.read())
                             
cur = conn.cursor()

df = pd.read_csv('Aarons Stuff/CleanHistGasPrices.csv')
df.to_sql('hist_gas_prices', conn, if_exists='append', index=False)

conn.commit()
conn.close()