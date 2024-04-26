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

sql_command = "INSERT INTO student(name, id) VALUES(%s, %s)"
data = ("Abdo Ezzat", 484)
myCursor = myConn.cursor()

# if you need to insert list of data you use executemany()
myCursor.execute(sql_command, data)
myConn.commit()
print("data inserted successfully")
print(myCursor.rowcount)
print(myCursor.lastrowid)