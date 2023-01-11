""" 
Created on : 09/12/22 4:52 AM
@author : ds  
"""
import unittest
from Dec_09_inheritance import BasicPlan,StandardPlan,PremiumPlan


class TestVideoStreamingPlans(unittest.TestCase):

    def test_basic_plan(self):
        self.assertEqual(BasicPlan.can_stream, True)
        self.assertEqual(BasicPlan.can_download, True)
        self.assertEqual(BasicPlan.num_of_devices, 1)
        self.assertEqual(BasicPlan.has_SD, True)
        self.assertEqual(BasicPlan.has_HD, False)
        self.assertEqual(BasicPlan.has_UHD, False)
        self.assertEqual(BasicPlan.price, '$8.99')

    def test_standard_plan(self):
        self.assertEqual(StandardPlan.can_stream, True)
        self.assertEqual(StandardPlan.can_download, True)
        self.assertEqual(StandardPlan.num_of_devices, 2)
        self.assertEqual(StandardPlan.has_SD, True)
        self.assertEqual(StandardPlan.has_HD, True)
        self.assertEqual(StandardPlan.has_UHD, False)
        self.assertEqual(StandardPlan.price, '$12.99')

    def test_premium_plan(self):
        self.assertEqual(PremiumPlan.can_stream, True)
        self.assertEqual(PremiumPlan.can_download, True)
        self.assertEqual(PremiumPlan.num_of_devices, 4)
        self.assertEqual(PremiumPlan.has_SD, True)
        self.assertEqual(PremiumPlan.has_HD, True)
        self.assertEqual(PremiumPlan.has_UHD, True)
        self.assertEqual(PremiumPlan.price, '$15.99')
