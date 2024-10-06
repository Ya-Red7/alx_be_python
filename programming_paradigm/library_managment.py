class Book:
    def __init__(self,title,author):
        self._is_checked_out = {}
        self.author = author
        self.title = title
        self.di2 = {}
    def checker(self):
        self._is_checked_out[self.title] = True
        self.di2[self.title] = self.author

class Library:
    def __init__(self):
        self._books = []
    def add_book(self,title,author):
        self._books.append([self.title,self.author])
