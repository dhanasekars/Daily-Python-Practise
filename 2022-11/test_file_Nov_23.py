""" 
Created on : 23/11/22 6:40 AM
@author : ds  
"""
import unittest
from Nov_23 import Book


class TestBook(unittest.TestCase):

    def test_title(self):
        PP = Book("Pride and Prejudice", "Jane Austen")
        H = Book("Hamlet", "William Shakespeare")
        self.assertEqual(PP.title, "Pride and Prejudice")
        self.assertEqual(H.title, "Hamlet")

    def test_author(self):
        PP = Book("Pride and Prejudice", "Jane Austen")
        H = Book("Hamlet", "William Shakespeare")
        self.assertEqual(PP.author, "Jane Austen")
        self.assertEqual(H.author, "William Shakespeare")

    def test_get_title(self):
        WP = Book("War and Peace", "Leo Tolstoy")
        HP = Book("Harry Potter", "J.K.Rowling")
        self.assertEqual(WP.get_title(), "Title: War and Peace")
        self.assertEqual(HP.get_title(), "Title: Harry Potter")

    def test_get_author(self):
        WP = Book("War and Peace", "Leo Tolstoy")
        HP = Book("Harry Potter", "J.K.Rowling")
        self.assertEqual(WP.get_author(), "Author: Leo Tolstoy")
        self.assertEqual(HP.get_author(), "Author: J.K.Rowling")