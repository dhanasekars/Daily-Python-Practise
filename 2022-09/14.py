""" 
Created on : 14/09/22 9:49 AM
@author : ds  
"""
import socket

test_data = '208.67.222.222'


def get_domain(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except Exception:
        pass


print(get_domain(test_data))