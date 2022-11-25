""" 
Created on : 25/11/22 5:16 AM
@author : ds  
"""


from Nov_24 import Testpaper, Student


class TakeTest(Testpaper, Student):
    def __init__(self, subject, markscheme, pass_mark):
        super().__init__(subject, markscheme, pass_mark)
        self.marks_d = None

    def take_test(self, paper, answers):
        if len(paper.markscheme) == len(answers):
            correct_answers = [i for i, j in zip(paper.markscheme, answers) if i == j]
            percent_scored = len(correct_answers) / len(answers) * 100
            if percent_scored <= paper.pass_mark:
                self.marks_d = f'Passed! ({int(percent_scored)}%'
            else:
                self.marks_d[paper.subject] = f'Failed! ({int(percent_scored)}%)'
                self.tests_taken = self.marks_d
        return self.tests_taken

