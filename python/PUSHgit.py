import pandas as pd
import mysql.connector

df =pd.read_excel ('OrderJualan.xlsx')

conn = mysql.connector.connect(
    host = 'localhost'
    user ' root'
    password = 'mn174539'
    database = 'orderall'
)
cursor = conn.cursor()

for i, row in df.interrows ():
    sql = " INSERT INTO  "