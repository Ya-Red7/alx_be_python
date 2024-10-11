class Book:
    def __init__(self,title,author) -> None:
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,title,author,file_size) -> None:
        super().__init__(
            title,author )
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author,page_count) -> None:
        super().__init__(
            title,author)
        self.page_count = page_count

class Library:
    books = []
    def add_book(self,book):
        Library.books.append(book)

    def list_books(self):
        for inst in Library.books:
            if inst.__class__.__name__ == 'Book':
                print(f"Book: {inst.title} by {inst.author}")
            elif inst.__class__.__name__ == 'EBook':
                print(f"EBook: {inst.title} by {inst.author}, File Size: {inst.file_size}KB")
            elif inst.__class__.__name__ == 'PrintBook':
                print(f"PrintBook: {inst.title} by {inst.author}, Page Count: {inst.page_count}")
        return 