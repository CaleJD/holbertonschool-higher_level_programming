#!/usr/bin/python3
"""Lists the cities of a given state from hbtn_0e_4_usa, sorted by id."""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (state_name,))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()
