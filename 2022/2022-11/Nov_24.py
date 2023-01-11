""" 
Created on : 24/11/22 5:25 AM
@author : ds  
"""


# https://edabit.com/challenge/Ld4xBpqBXqygwQ5St
# Program that allows teachers to create a multiple choice test in a class called
# 'Testpaper' and able to assign minimum pass mark.


class Testpaper:
    """
    class to create test paper with attributes 'subject', 'markscheme' and 'pass_mark"
    """

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = float(pass_mark.strip('%'))
