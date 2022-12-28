""" 
Created on : 28/12/22 8:33 AM
@author : ds
https://www.youtube.com/watch?v=nlCKrKGHSSk
"""

import logging
import time

#create logger

logging.basicConfig(filename="/Users/ds/Documents/problems.log", level=logging.DEBUG)
logger = logging.getLogger()


def read_file_timed(path):
    """
    Return the content of the file at 'path and measure time required to open
    :param path:
    :return:
    """
    start_time = time.time()
    try:
        f = open(path, mode ="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"Time required for {path} = {dt}")


read_file_timed("/Users/ds/Movies/4K Video Downloader/LIVEமுதலமைச்சர் தலைமையில் சென்னை சூப்பர் கிங்ஸ் அணியினருக்கு "
                "பாராட்டுவிழா.mp4")
