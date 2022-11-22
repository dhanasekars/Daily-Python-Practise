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
        self.currentPage = 1
        self.total = 0
        self.getTotalPages()
        self.pages = self.createPages()

    def getItems(self):
        return self.items

    def getPageSize(self):
        return self.pageSize

    def getCurrentPage(self):
        pass

    def getTotalPages(self):
        if len(self.items) % self.pageSize:
            self.total = len(self.items) // self.pageSize + 1
        else:
            self.total = len(self.items) // self.pageSize
        return self.total

    def createPages(self):
        pages = [self.items[i * self.pageSize:(i + 1) * self.pageSize]
                 for i in range((len(self.items) + self.pageSize - 1) // self.pageSize)]
        return pages


# alphabetList = list("abcdefghijklmnopqrstuvwxy")
# p1 = Pagination(alphabetList, 4)
# print(p1.createPages())



