#!/usr/bin/python
import mysql.connector

import sys

dbname = str(sys.argv[1]);


cnx = mysql.connector.connect(user='purva', password='password',host='127.0.0.1',                          database=dbname)

cursor = cnx.cursor()

query = ("select table_name,table_rows from information_schema.tables where table_schema = '" + dbname + "'")

cursor.execute(query)
for (table_name,table_row) in cursor:
	print ("Table '" + table_name + "' has " + str(table_row) +" rows.")


cursor.close()
cnx.close()
