""" 
Created on : 08/12/22 5:21 AM
@author : ds  
"""

import random

#
# class AvoidExec:
#     def __init__(self):
#         self.txt = None
#         self.users = None
#         self.site = {
#             'Python Crash Course': 'Eric Matthes',
#             'Automate the Boring Stuff': 'Al Sweigart',
#             'Learning Python': 'Mark Lutz'
#         }
#         self.param = "\"); res = users #"
#         self.exec_search(search=self.search)
#
#     def search(self, txt):
#         self.txt = txt.lower()
#         return {k: v for k, v in self.site.items() if self.txt in (k + ' ' + v).lower()}
#
#     def exec_search(self, search):
#         for _ in range(14):
#             self.users = {'user %s' % k: 'password' + str(random.randrange(10, 100)) for k in range(5)}
#             exec('res = search("%s")' % self.param)


# working descriptive code

import random

site = {
    'Python Crash Course': 'Eric Matthes',
    'Automate the Boring Stuff': 'Al Sweigart',
    'Learning Python': 'Mark Lutz'
}

param = '"); res = users #'

def search(txt):
    txt = txt.lower()
    return {
        k: v for k, v in site.items()
        if txt in (k + ' ' + v).lower()
    }


for _ in range(14):
    users = {
        'user %s' % k: 'password' + str(random.randrange(10, 100))
        for k in range(5)
    }
    exec('res = search("%s")' % param)
    print(res == users)
