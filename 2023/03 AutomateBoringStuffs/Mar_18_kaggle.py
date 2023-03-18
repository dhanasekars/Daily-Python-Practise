""" 
Created on : 18/03/23 11:20 am
@author : ds  
"""

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
print(api.authenticate())
api.competition_download_file(competition='home-data-for-ml-course',
                              file_name='sample_submission.csv')
