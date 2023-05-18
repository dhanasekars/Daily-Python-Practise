""" 
Created on : 18/05/23 5:49 am
@author : ds  
"""

import os
from datetime import datetime
file_path = "/Users/ds/PycharmProjects/DailyChallenge/2023/05 Packages/18_meta_data.py"
timestamp = 1545730073

def display_meta_data(filepath):
    file_stat = os.stat(filepath)
    file_created = datetime.fromtimestamp(file_stat.st_birthtime).strftime("%Y-%m-%d %H:%M:%S")
    file_modified = datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    file_accessed = datetime.fromtimestamp(file_stat.st_atime).strftime("%Y-%m-%d %H:%M:%S")

    return {"File": filepath, "Size": str(round(file_stat.st_size / 1024, 2))+' KBs', "Created": file_created,
            'Last Modified': file_modified, 'Last Accessed': file_accessed}


for key, value in display_meta_data(filepath=file_path).items():
    print(f"{key} : {value}")