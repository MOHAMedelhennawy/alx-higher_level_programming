#/usr/bin/python3

'''
This program to learn how to connect to Database,
and how to create new DB
'''

import mysql.connector

myConn = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "root",
)

myCursor = myConn.cursor()
myCursor.execute("SHOW DATABASES")

for db in myCursor:
    print(db)