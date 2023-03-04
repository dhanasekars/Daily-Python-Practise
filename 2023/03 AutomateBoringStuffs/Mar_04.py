""" 
Created on : 04/03/23 5:08 AM
@author : ds  
"""

# DONE Day 4 - Move files to a new location
# DONE Day 4 - Pass list of list to be zipped


from Mar_02 import weekly_backup
from Mar_03 import zip_folder
from config import WEEKLY
import logging

# Logging config
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=WEEKLY.logging_file_path, level=logging.DEBUG, format=LOG_FORMAT, filemode='a')

if __name__ == '__main__':
    try:
        weekly_backup()
        for path in WEEKLY.folders_list:
            zip_folder(path[0], path[1])
    except Exception as e:
        logging.exception(e)
    finally:
        logging.info("Weekly backup completed")


