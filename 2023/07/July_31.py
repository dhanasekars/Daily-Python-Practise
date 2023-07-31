""" 
Created on : 31/07/23 1:35 pm
@author : ds  
"""

import sqlite3

conn = sqlite3.connect("members.db")
cur = conn.cursor()

with open("test.sql") as file:
    sql_script = file.read()

cur.executescript(sql_script)

cur.close()
conn.close()