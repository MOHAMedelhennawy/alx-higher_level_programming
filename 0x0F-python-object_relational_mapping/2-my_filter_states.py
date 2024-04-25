#!/usr/bin/python3
'''
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    myCursor.execute("SELECT * FROM states WHERE name LIKE '{}'".format(argv[4]))
    result = myCursor.fetchall()

    for res in result:
        print(res)

    myCursor.close()
    myConn.close()
