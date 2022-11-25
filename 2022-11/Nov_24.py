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


class Student:
    """
    student class for students to take tests.
    """
    marks_d = {}

    def __init__(self, tests_taken="None"):
        self.tests_taken = "No tests taken" if tests_taken == "None" else tests_taken

    # For Nov 24

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


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Physics", ["1B", "2A", "3D", "4B", "5C"], "80%")

student1 = Student()

student1.take_test(paper1, ["1A", "2C", "3D", "4B", "5A"])
student1.take_test(paper2, ["1B", "2B", "3D", "4B", "5A"])
print(student1.tests_taken)
