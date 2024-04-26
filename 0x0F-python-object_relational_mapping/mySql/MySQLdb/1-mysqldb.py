#/usr/bin/python3

'''
This program to learn how to connect to Database
'''

import mysql.connector

myConn = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "root",
)

myCursor = myConn.cursor()
print("COnnected")
