""" 
Created on : 09/12/22 4:52 AM
@author : ds  
"""

class BasicPlan:
    can_stream = True
    can_download = True
    num_of_devices = 1
    has_SD = True
    has_HD = False
    has_UHD = False
    price = '$8.99'

class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '$12.99'


class PremiumPlan(StandardPlan):
    has_UHD = True
    num_of_devices = 4
    price = '$15.99'



