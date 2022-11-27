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

    def take_test(self, paper: Testpaper, answers: list):
        self.answers = answers
        if len(paper.markscheme) == len(self.answers):
            correct_answers = len([i for i, j in zip(paper.markscheme, answers) if i == j])
            percentage_scored = correct_answers / len(answers) * 100
            if percentage_scored >= float(paper.pass_mark.strip('%')):
                self.my_d[paper.subject] = 'Passed! ({}%)'.format(round(float(percentage_scored)))
            else:
                self.my_d[paper.subject] = 'Failed! ({}%)'.format(round(float(percentage_scored)))

        self.tests_taken = self.my_d
        return self.tests_taken


# OTHER BETTER APPROACHES


# class Testpaper:
#
#     def __init__(self, subject, markscheme, pass_mark):
#         self.subject = subject
#         self.markscheme = markscheme
#         self.pass_mark = pass_mark
#
#
# class Student:
#     tests_taken = 'No tests taken'
#
#     def take_test(self, paper, choices):
#         score = len(set(paper.markscheme) & set(choices)) / len(paper.markscheme)
#         result = 'Passed!' if score >= int(paper.pass_mark[:-1]) / 100 else 'Failed!'
#         percent = '{:.0%}'.format(score)
#
#         if self.tests_taken == 'No tests taken':
#             self.tests_taken = {paper.subject: '{} ({})'.format(result, percent)}
#         else:
#             self.tests_taken[paper.subject] = '{} ({})'.format(result, percent)

# class Testpaper:
#     def __init__(self, subject, markscheme, pass_mark):
#         self.subject = subject
#         self.markscheme = markscheme
#         self.pass_mark = pass_mark
#
#
# class Student:
#     def __init__(self):
#         self.tests_taken = 'No tests taken'
#
#     def take_test(self, paper, answers):
#         pmark = int(paper.pass_mark[:-1])
#         correct = sum(a == b for a, b in zip(paper.markscheme, answers))
#         perc = '{:.0%}'.format(correct / len(answers))
#         msg = '{}! ({})'.format('Passed' if int(perc[:-1]) > pmark else 'Failed', perc)
#
#         if type(self.tests_taken) == str:
#             self.tests_taken = {paper.subject: msg}
#         else:
#             self.tests_taken[paper.subject] = msg