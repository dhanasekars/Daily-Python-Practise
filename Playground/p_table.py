""" 
Created on : 18/04/23 12:22 pm
@author : ds  
"""

from prettytable import PrettyTable

X = PrettyTable()

X.add_column("City Name", ["Adelaide", "Brisbane", "Hobart", " Sydney", "Perth"])
print(X.get_html_string())

with open("../ascii.txt", 'w') as file:
    file.write(X.get_string())

