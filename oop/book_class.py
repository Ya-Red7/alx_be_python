class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
<<<<<<< HEAD
        return f"Book('{self.title}', '{self.author}', {self.year})"
=======
        return f"Book('{self.title}', '{self.author}', {self.year})"
>>>>>>> ecacd17c3f8630cbfabe735fdc3f0ce3faafee92
