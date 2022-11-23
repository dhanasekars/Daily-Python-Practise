""" 
Created on : 23/11/22 6:39 AM
@author : ds  
"""

# https://edabit.com/challenge/uK4Dw7Pise5uCfKqo


class Book:
    """
     Book class has two attributes .title and .author, and two methods
    .get_title() returns "Title: " + instance title
    .get_author() returns "Author: " + instance author
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        """
        :return: String --> "Title: <instance title>"
        """
        return "Title: {}".format(self.title)

    def get_author(self):
        """
        :return: String --> "Author: <instance author>"
        """
        return "Author: {}".format(self.author)

