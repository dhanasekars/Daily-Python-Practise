""" 
Created on : 25/11/22 5:50 AM
@author : ds  
"""


class Testpaper:

    def __init__(self, subject, markscheme, pass_mark) -> None:
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    global my_d
    my_d = {}

    def __init__(self, tests_taken='No tests taken') -> None:
        self.tests_taken = "No tests taken" if tests_taken == "None" else tests_taken

    def take_test(self, paper, answers):
        if len(paper.markscheme) == len(answers):
            correct = [i for i, j in zip(paper.markscheme, answers) if i == j]
            calc = len(correct) / len(answers) * 100
            expected_perc = float(paper.pass_mark.strip('%'))
            if expected_perc <= calc:
                my_d[paper.subject] = f'Passed! ({int(calc)}%)'
                self.tests_taken = my_d
                return self.tests_taken
            else:
                my_d[paper.subject] = f'Failed! ({int(calc)}%)'
                self.tests_taken = my_d
                return self.tests_taken


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Physics", ["1B", "2A", "3D", "4B", "5C"], "80%")

student1 = Student()
student2 = Student()
student3 = Student()

student1.take_test(paper1, ["1A", "2C", "3D", "4B", "5A"])
student1.take_test(paper2, ["1B", "2B", "3D", "4B", "5A"])
print(student1.tests_taken)

student2.take_test(paper1, ["1B", "2E", "3D", "4A", "5A"])
print(student2.tests_taken)

print(student3.tests_taken)