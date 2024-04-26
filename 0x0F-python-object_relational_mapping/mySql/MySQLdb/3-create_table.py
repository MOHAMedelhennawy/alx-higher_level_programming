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
    database = "school"   
)

myCursor = myConn.cursor()
myCursor.execute("CREATE TABLE student (name VARCHAR(30), id INT)")

print("Table created successfully")