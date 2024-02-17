#!/usr/bin/python3
""" Querying from states table in a specified database """
if __name__ != "__main__":
    exit()
import MySQLdb
import sys

args = sys.argv
conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * from states ORDER BY states.id;")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
