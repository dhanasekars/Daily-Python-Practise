"""
Created by: DS
Created at: 2023-06-21 13:09:28

This code is explore an option to connect postgresql to python code
using pyscopg2.

As of June 21, 2023 there is no active posgres installed locally, need to revisit this in the coming weekend
after having an active postgresql server running.

"""

import psycopg2

conn = psycopg2.connect(host, port, database, user, password )

cursor = conn.cursor()

cursor.execute("SELECT * FROM test_table")
rows = cursor.fetchall()

for row in rows:
    print(row)