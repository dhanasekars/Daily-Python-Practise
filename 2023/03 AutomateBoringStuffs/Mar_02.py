""" 
Created on : 02/03 AutomateBoringStuffs/23 5:06 AM
@author : ds  
"""

# DONE Day 2 - Rename two folders inside a given folder path
# DONE Day 2 - create logging
# TODO Day 3 - Exception handling
# TODO Day 3 - Move folders to a new location
# TODO Day 4 - Zip folders
# TODO Day 5 - Pass dictionary of files to be deleted and renamed

from config import WEEKLY  # import config file
import os
import shutil
from time import sleep
import logging

# Logging config
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=WEEKLY.logging_file_path, level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()

def weekly_backup():
    """
    I do a weekly backup of certain folders from my icloud to gDrive and dropbox.
    Automate the backup process.
    :return: None
    """
    logger.info("Starting the weekly backup process")

    # delete folder Week 2
    logger.debug("Deleting folder Week 2")
    shutil.rmtree(WEEKLY.folder_to_delete)

    # rename folder Week 1 to Week 2
    logger.debug("Renaming folder Week 1 to Week 2")
    os.rename(WEEKLY.folder1_to_rename, WEEKLY.weekly_backup_path+'/test 2')

    # rename folder Week 0 to Week 1
    logger.debug("Renaming folder Week 0 to Week 1")
    os.rename(WEEKLY.folder0_to_rename, WEEKLY.weekly_backup_path+'/test 1')

    # create folder Week 0
    logger.debug("Creating folder Week 0")
    os.makedirs(WEEKLY.weekly_backup_path+'/test 0')
    logger.info("Weekly backup folder changes completed")
    return None


