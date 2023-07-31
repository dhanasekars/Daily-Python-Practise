""" 
Created on : 31/07/23 1:17 pm
@author : ds  
"""

import sqlite3

# connect to a new database
conn = sqlite3.connect("demo.db")

#  create a cursor
cur = conn.cursor()

# Create a 'people' table

cur.execute('''CREATE TABLE IF NOT EXISTS people 
(first_name TEXT, last_name TEXT)''')
conn.commit()

# Test data

names_list = [("Dhanasekar", "Subramaniam"),
              ("Kanimozhi", "Nadia"),
              ("DS", ""),
              ("Kavipriya", "Ganeshkumar")]

cur.executemany(''' INSERT INTO people (first_name, last_name) VALUES (?,?)''', names_list)
cur.close()
conn.close()