""" 
Created on : 07/06/23 6:37 pm
@author : ds  
"""

from June_07 import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('June_07.os.path')
    @mock.patch('June_07.os')

    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False

        rm("any path")

        self.assertFalse(mock_os.remove.called, "Faile to not remove the file if not present")

        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")


