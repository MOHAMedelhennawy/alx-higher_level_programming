#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    myConn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306,
    )

    myCursor = myConn.cursor()
    myCursor.execute("SELECT * FROM states ORDER BY id")
    rows = myCursor.fetchall()

    for row in rows:
        print(row)

    myCursor.close()
    myConn.close()
