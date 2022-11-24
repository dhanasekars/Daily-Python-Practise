""" 
Created on : 24/11/22 5:25 AM
@author : ds  
"""

# Program that allows teachers to create a multiple choice test in a class called
# 'Testpaper' and able to assign minimum pass mark.


class Testpaper:
    """
    class to create test paper with attributes 'subject', 'markscheme' and 'pass_mark"
    """
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    """
    student class for students to take tests.
    """
    def __init__(self, tests_taken="None"):
        self.tests_taken = "No tests taken" if tests_taken == "None" else tests_taken

    # For Nov 24
    def take_test(self):
        pass



