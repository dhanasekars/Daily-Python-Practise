""" 
Created on : 26/11/22 4:43 AM
@author : ds  
"""

# https://edabit.com/challenge/kbtju9wk5pjGYMmHF


class Name:
    """
    Have two attributes first name and last name as fname and lname
    An attribute called fullname which returns the first and last names.
    An attribute called initials which returns the first letters of the
    first and last name. Put a . between the two letters.
    The attributes fname and lname to be accessed individually as well.
    """

    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = f"{self.fname} {self.lname}"
        self.initials = f"{self.fname[0]}.{self.lname[0]}"

