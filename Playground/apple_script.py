""" 
Created on : 07/03/23 3:50 PM
@author : ds  
"""

import os

# Write a function to send a desktop notifation using apple scripts


def send_desktop_notification(title, text):
    os.system("""
    osascript -e 'display notification "{}" with title "{}"  sound name "Glass" ' """
               .format(text, title))


send_desktop_notification("Mad Message", "There is a failure in the script. How are you doing? I will fix it tomorrow.")
