""" 
Created on : 20/11/22 5:34 AM
@author : ds  
"""
from Nov_20 import Pagination


class ExtendPagination(Pagination):

    def goToPage(self, pageNo=1):
        if pageNo > self.total:
            self.currentPage = self.total
        elif pageNo < 1:
            self.currentPage = 1
        else:
            self.currentPage = pageNo
        return self.currentPage

    def getVisibleItems(self):
        return self.pages[self.currentPage - 1]

    def prevPage(self):
        if self.currentPage != 1:
            self.currentPage = self.currentPage - 1

    def nextPage(self):
        if self.currentPage != self.totalPages:
            self.currentPage = self.currentPage + 1


alphabetList = list("abcdefghijklmnopqrstuvwxy")
ePagination = ExtendPagination(alphabetList, 4)
print(ePagination.getVisibleItems())

# Nov 22 : Make double inheritance
# Add gotoPage
# Add First-page
# Add last-page

# Nov 23 : Tests for all methods
