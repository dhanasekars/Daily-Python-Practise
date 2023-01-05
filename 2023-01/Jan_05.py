""" 
Created on : 05/01/23 11:26 AM
@author : ds
https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true
"""


class EvenStream(object):

    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):

    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


"""
Buggy code
def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())
"""

### Solution
### Reason --> the default argument is evaluated only once when the function is defined.
# https://docs.python-guide.org/writing/gotchas/


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

# Alternative approach is to init the stream every time
"""
def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())
"""

print_from_stream(3)