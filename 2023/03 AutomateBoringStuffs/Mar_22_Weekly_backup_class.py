""" 
Created on : 22/03/23 8:41 am
@author : ds  
"""
import logging
from config import WEEKLY
import os
import shutil
from datetime import datetime

# Logging config
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=WEEKLY.logging_file_path, level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()


class WeeklyBackup:
    """Backup Weekly Servers"""

    def __init__(self):
        pass

    def send_desktop_notification(self):
        date_string = datetime.today().strftime("%d-%b-%Y %I:%M:%S %p")

        os.system("""
        osascript -e 'display notification "{}" with title "{}"  sound name "Glass" ' """
                  .format(self, date_string))
