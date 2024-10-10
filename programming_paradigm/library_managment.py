'''class Book:
    def __init__(self,title,author):
        self._is_checked_out = False
        self.author = author
        self.title = title
    def checker(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def returner(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return False
        return True
    def isAvailable(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._books = []
    def add_book(self,book):
        self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if book.title==title:
                if book.checker():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")
    def return_book(self,title):
        for book in self._books:
            if book.title==title:
                if book.returner():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is already returned.")
                return
        print(f"'{title}' not found in the library.")
    def list_available_books(self):
        books = [book for book in self._books if book.isAvailable()]
        if books:
            for book in books:
                print(f"{book.title} by {book.author}")
        else:
            print("None available")'''
# Python program to demonstrate 
# duck typing 


class Bird: 
	def fly(self): 
		print("fly with wings") 

class Airplane: 
	def fly(self): 
		print("fly with fuel") 

class Fish: 
	def swim(self): 
		print("fish swim in sea") 
class f(Bird,Airplane):
  pass
ff = f()
# Attributes having same name are 
# considered as duck typing 
for obj in f: 
	obj.fly() 
