""" 
Created on : 13/04/23 8:40 am
@author : ds  
"""
import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
conn.system.methodSignature('phone')
print(conn.phone('Bert'))

### 555-ITALY

# http://www.pythonchallenge.com/pc/return/italy.html