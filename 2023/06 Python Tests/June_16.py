""" 
Created on : 16/06/23 5:37 pm
@author : ds  
"""
import os
import os.path

class RemovalService(object):

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    class UploadService(object):

        def __init__(self, removal_service):
            self.removal_service = removal_service

        def upload_complete(self, filename):
            self.removal_service.rm(filename)
