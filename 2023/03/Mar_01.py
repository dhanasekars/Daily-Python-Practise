""" 
Created on : 01/03/23 4:23 AM
@author : ds  
"""

# TODO Day 1 - create config file to store folder paths
# TODO Day 1 - Function should delete a folder and rename two folders inside a given folder path
# TODO Day 2 - log details
# TODO Day 3 - Exception handling
# TODO Day 4 - Pass dictionary of files to be deleted and renamed with location

from pathlib import Path
import os

def weekly_backup():
    """
    I do a weekly backup of certain folder from my icloud to gDrive and dropbox.
    Automate the backup process
    :return:
    """
    os.makedirs('/Users/ds/Library/CloudStorage/GoogleDrive-email@dhanasekars.com'
                '/My Drive/Focused Life Backup/test folder')
    return Path.home()

print(weekly_backup())

