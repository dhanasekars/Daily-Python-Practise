"""
Created by: DS
Created at: 2023-06-21 13:09:28

This code is explore an option to connect postgresql to python code
using pyscopg2.

As of June 21, 2023 there is no active posgres installed locally, need to revisit this in the coming weekend
after having an active postgresql server running.

A cloud Postgres was setup in a DBaaS (elephantSQL) and a connection was established on June 22, 2023


"""

import psycopg2
from config import Postgresql

conn = psycopg2.connect(
    host=Postgresql.elephantsql_url, 
    port=Postgresql.elephantsql_port,
    database=Postgresql.database,
    user=Postgresql.user,
    password=Postgresql.password )

cursor = conn.cursor()

cursor.execute("SELECT * FROM COMPANY;")
rows = cursor.fetchall()

for row in rows:
    print(row)