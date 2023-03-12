""" 
Created on : 01/03 AutomateBoringStuffs/23 4:23 AM
@author : ds  
"""

# DONE Day 1 - create config file to store folder paths
# DONE Day 1 - Function should delete a folder
# TODO Day 2 - Rename two folders inside a given folder path
# TODO Day 2 - create logging
# TODO Day 3 - Exception handling
# TODO Day 4 - Pass dictionary of files to be deleted and renamed

from config import WEEKLY
import os
import shutil
from time import sleep
def weekly_backup():
    """
    I do a weekly backup of certain folders from my icloud to gDrive and dropbox.
    Automate the backup process.
    :return:
    """
    os.makedirs(WEEKLY.weekly_backup_path+'/test')
    print("a test folder is created")
    sleep(3)
    print('The folder is about to get deleted....')
    shutil.rmtree(WEEKLY.folder_to_delete)
    print('One less boring job for you...')
    return None






