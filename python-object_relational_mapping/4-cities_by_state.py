#!/usr/bin/python3
"""Lists all cities in the hbtn_0e_0_usa database sorted by id."""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "INNER JOIN states on cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
