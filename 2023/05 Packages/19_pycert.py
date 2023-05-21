""" 
Created on : 16/05/23 4:42 pm
@author : ds  
"""
from pycert import CertClient
from pprint import pprint

cert = CertClient('moolya.com')
pprint(cert.get_all_info())
pprint(cert.get_serial_number())

pprint(cert.get_signature_algorithm())