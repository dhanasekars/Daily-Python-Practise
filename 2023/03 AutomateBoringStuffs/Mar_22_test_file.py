""" 
Created on : 22/03/23 8:55 am
@author : ds  
"""

from Mar_22_Weekly_backup_class import WeeklyBackup
import unittest


class TestWeeklyBackup(unittest.TestCase):

    def test_desktop_notification(self):
        self.assertEqual(None, WeeklyBackup.send_desktop_notification('test'))


backup1 = WeeklyBackup()
