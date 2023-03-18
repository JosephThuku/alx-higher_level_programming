#!/usr/bin/python3
"""
Python script that lists all states from database hbtn_0e_usa
"""
import MySQLdb
import sys

def main():
    input = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    cur = db.cursor()
    cur.execute("""
    SELECT *
    FROM states
    WHERE name=%s
    ORDER BY states.id""", (input,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
