"""
Created on : 08 graphQL/06/23 5:05 am
@author : ds  
"""
from June_08_greek import sinusoid
import unittest


class TestSinuoid(unittest.TestCase):

    def test_zeros(self):
        waveform = sinusoid(0, 0, 0)
        self.assertEqual(0, waveform(0))

    def test_ones(self):
        waveform = sinusoid(1, 1, 1)
        self.assertAlmostEqual(0.9092974, waveform(1))
