#!/usr/bin/python3
"""
Python script that lists cities by states
"""
import MySQLdb
import sys

state_name = sys.argv[4]
db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
cur = db.cursor()
cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id", (state_name,))
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
