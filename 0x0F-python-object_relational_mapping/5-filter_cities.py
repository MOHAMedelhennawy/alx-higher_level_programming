#!/usr/bin/python3
'''
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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

    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            WHERE states.name LIKE %s"

    myCursor = myConn.cursor()
    myCursor.execute(query, (argv[4],))
    rows = myCursor.fetchall()
    tmp = [row[0] for row in rows]
    print(*tmp, sep=', ')

    myCursor.close()
    myConn.close()
