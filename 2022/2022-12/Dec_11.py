""" 
Created on : 11/12/22 5:08 AM
@author : ds
https://edabit.com/challenge/NAhsYH4q4jtaQB7Bf
"""


class Lever:
    """
    Levers are simple machines with a rigid beam and a fulcrum. From the picture below,
    you can see that there are 3-types of levers: first class, second class and third class.
    First class lever, the fulcrum is in the middle with the effort and the load being positioned opposite of each other
    Second class lever, the fulcrum is situated in the right with the effort on the left and the load in the middle.
    Third class lever, the fulcrum is in the left with the effort being in the middle and the load being on the right.
    """

    def __init__(self):
        self.lever = None

    def SetLever(self, lst):
        self.lever = lst

    def GetLever(self):
        return self.lever

    def determine_lever(self):
        return ("third", "first", "second")[self.lever.index('f')] + " class lever"
