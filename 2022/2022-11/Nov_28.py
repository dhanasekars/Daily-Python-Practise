""" 
Created on : 28/11/22 5:17 AM
@author : ds  
"""

# https://edabit.com/challenge/gB7nt6WzZy8TymCah


class Employee:
    """
    Form the fullname by simply joining the first and last name together, separated by a space.
    Form the email by joining the first and last name together with a "dot" --> . in between,
    and follow it with @company.com at the end. Make sure the entire email is in lowercase.
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = "{} {}".format(firstname, lastname)
        self.email = "{}.{}@company.com".format(firstname, lastname).lower()


