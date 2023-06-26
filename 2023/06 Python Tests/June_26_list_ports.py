""" 
Created on : 26/06/23 9:18 am
@author : ds  
"""
import psutil

# Get all the running processes & the port it us listening

processes = psutil.process_iter(['pid', 'name', 'username', 'connections'])
for process in processes:
    try:
        print(process.info)
        connections = process.info['connections']
        if connections is not None:
            for conn in connections:
                if conn.status == "LISTEN":
                    print(conn)
                    print(f"Process: {process.info['name']} | Port : {conn.laddr.port} ")
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

