""" 
Created on : 20/11/22 5:34 AM
@author : ds  
"""


class Pagination:

    def __init__(self, items=None, pageSize=10.0):
        if items is None:
            items = []
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 0
        self.total = 0

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        pass

    # This is for Nov 20

    def getTotalPages(self):
        if len(self.items) % self.pageSize:
            self.total = len(self.items) // self.pageSize + 1
        else:
            self.total = len(self.items) // self.pageSize
        return self.total

    # This is for Nov 21

    def goToPage(self, pageNo=1):
        pass


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.goToPage(3))

