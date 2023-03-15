""" 
Created on : 15/03/23 10:09 am
@author : ds  
"""


import logging
import sh

from config import WEEKLY, GitHubDetails

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=WEEKLY.logging_file_path, level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()

git = sh.git.bake(_cwd=GitHubDetails.second_brain)


# git.diff("--exit-code", "--exit-code", _in=True)

# Check if there are any changes in the working tree and then add, commit to the repo
if git.status("--porcelain"):
    logger.debug(git.add('-A'))
    logger.debug(git.commit(m='weekly commit'))
    logger.debug(git.push('-u', 'origin', 'main'))
else:
    logger.info("nothing to commit")
