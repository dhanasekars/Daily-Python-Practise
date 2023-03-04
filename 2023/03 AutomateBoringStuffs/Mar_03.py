"""
Created on : 03 AutomateBoringStuffs/03 AutomateBoringStuffs/23 5:14 AM
@author : ds  
"""
# DONE Day 3 - Exception handling
# DONE Day 3 - Zip folders
# TODO Day 4 - Move files to a new location
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

def zip_folder(folder_path, file_name):
    """
    Zip a folder
    :param file_name:
    :param folder_path:
    :return:
    """
    logger.info("Zipping folder {}".format(folder_path))
    shutil.make_archive(WEEKLY.week0 + file_name, 'zip', folder_path)
    logger.info("Zipping completed")
    return None

