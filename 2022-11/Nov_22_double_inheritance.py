""" 
Created on : 22/11/22 5:37 AM
@author : ds  
"""
from Nov_21_inheritance import ExtendPagination


class PageNavigation(ExtendPagination):

    def goToFirstPage(self):
        self.currentPage = 1
        return self.currentPage

    def goToLastPage(self):
        self.currentPage = self.total
        return self.currentPage


alphabetList = list("abcdefghijklmnopqrstuvwxy")
dPagination = PageNavigation(alphabetList, 4)


