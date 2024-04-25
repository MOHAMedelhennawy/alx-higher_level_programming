#!/usr/bin/python3
'''
script that lists all cities from the database hbtn_0e_4_usa
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

    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id"

    myCursor = myConn.cursor()
    myCursor.execute(query)
    rows = myCursor.fetchall()

    for row in rows:
        print(row)

    myCursor.close()
    myConn.close()
