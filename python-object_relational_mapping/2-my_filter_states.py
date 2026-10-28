#!/usr/bin/python3
"""Lists all values from states in the hbtn_0e_0_usa database, sorted by id."""

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
    cur.execute("SELECT * FROM states WHERE name = '{}' "
                "ORDER BY states.id ASC".format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
