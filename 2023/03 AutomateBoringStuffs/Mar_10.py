""" 
Created on : 10/03/23 5:06 AM
@author : ds  
"""

import os
from datetime import datetime


# Write a function to send a desktop notifation using apple scripts


def send_desktop_notification(text):
    date_string = datetime.today().strftime("%d-%b-%Y %I:%M:%S %p")

    os.system("""
    osascript -e 'display notification "{}" with title "{}"  sound name "Glass" ' """
              .format(text, date_string))


# The following script takes a string of text as an argument, sends a desktop
# notification, and then quits.

if __name__ == "__main__":
    send_desktop_notification("Weekly back up completed.")
