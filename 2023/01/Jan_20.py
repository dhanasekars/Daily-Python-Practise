""" 
Created on : 20/01/23 4:33 AM
@author : ds
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
"""

def gradingStudents(grades):
    """
    If the difference between the  grade and the next multiple of 5 is less than 3,
    round grade up to the next multiple of 5.
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
    :param grades:
    :return:
    """
    return [grade if grade < 38 or grade % 5 < 3 else grade + (5 - grade % 5) for grade in grades]

