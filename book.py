class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True
