"""
Created on : 26/11/22 12:54 PM
@author : ds
"""
""" 
Created on : 24/11/22 5:25 AM
@author : ds  
"""


# https://edabit.com/challenge/Ld4xBpqBXqygwQ5St
# Program that allows teachers to create a multiple choice test in a class called
# 'Testpaper' and able to assign minimum pass mark.

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:

    def __init__(self, tests_taken="None"):
        self.answers = None
        self.tests_taken = "No tests taken" if tests_taken == 'None' else tests_taken
        self.my_d = {}

    def take_test(self, paper, answers: list):
        self.answers = answers
        if len(paper.markscheme) == len(self.answers):
            correct_answers = len([i for i, j in zip(paper.markscheme, answers) if i == j])
            percentage_scored = correct_answers / len(answers) * 100
            if percentage_scored >= float(paper.pass_mark.strip('%')):
                self.my_d[paper.subject] = 'Passed! ({}%)'.format(int(percentage_scored))
            else:
                self.my_d[paper.subject] = 'Failed! ({}%)'.format(int(percentage_scored))

        self.tests_taken = self.my_d
        return self.tests_taken
