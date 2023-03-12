""" 
Created on : 12/03/23 5:32 am
@author : ds  
"""

import logging
import sh

from config import WEEKLY, GitHubDetails

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=WEEKLY.logging_file_path, level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()

git = sh.git.bake(_cwd=GitHubDetails.second_brain)
logger.info(git.status())
logger.info(git.add('-A'))
logger.info(git.commit(m='weekly commit'))
logger.info(git.push('-u', 'origin', 'main'))
