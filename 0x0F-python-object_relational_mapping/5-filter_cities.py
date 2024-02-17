#!/usr/bin/python3
""" Querying from states table in a specified database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv
    fname = args[4].split(sep=";")[0].rstrip("\"")

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id =" +
                " (SELECT states.id FROM states WHERE states.name = \"{}\")"
                .format(fname) +
                " ORDER BY cities.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end="")
        if row is not query_rows[-1]:
            print(", ", end="")
        else:
            print("")
    cur.close()
    conn.close()
