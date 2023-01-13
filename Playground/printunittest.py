import unittest

def staircase(n):
    """
    It is a function that prints a staircase of size n.
    : param n: An integer
    :Print a staircase as described above.
    The function should not return a value.
    """
    for i in range(1, n+1):
        print(" " * (n - i) + "#"*i)

class StaircaseTests(unittest.TestCase):
    def test_staircase_5(self):
        # Capture the output of the print statement
        with self.assertPrints("    #\n   ##\n  ###\n ####\n#####\n"):
            staircase(5)
    def test_staircase_3(self):
        with self.assertPrints("  #\n ##\n###\n"):
            staircase(3)
    def test_staircase_1(self):
        with self.assertPrints("#\n"):
            staircase(1)

