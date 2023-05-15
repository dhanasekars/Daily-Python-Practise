""" 
Created on : 06/05/23 6:38 am
@author : ds  
"""
import io
import csv

csv_data = 'Name,Age\nAlice,30\nBob,25\nCharlie,40\n'
csv_file = io.StringIO(csv_data)
reader = csv.DictReader(csv_file)

for row in reader:
    print(row)

output = io.StringIO()
output.write('First line.\n')
print('Second line.',file=output)
contents = output.getvalue()
print(contents)
output.close()