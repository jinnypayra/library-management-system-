from book import Book
from member import Member
from loan import Loan
from exceptions import *

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []
        self._loan_counter = 1

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"Book added: {title}"

    def register_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"Member registered: {name}"

    def borrow_book(self, book_id, member_id):
        book = self._books.get(book_id)
        if not book:
            raise BookNotFoundError("Book not found.")

        member = self._members.get(member_id)
        if not member:
            raise MemberNotFoundError("Member not found.")

        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")

        book.borrow()
        loan = Loan(self._loan_counter, book, member)
        self._loans.append(loan)
        self._loan_counter += 1
        return f"{member.name} borrowed {book.title}"

    def return_book(self, book_id, member_id):
        book = self._books.get(book_id)
        if not book:
            raise BookNotFoundError("Book not found.")

        member = self._members.get(member_id)
        if not member:
            raise MemberNotFoundError("Member not found.")

        active_loan = None
        for loan in self._loans:
            if loan.book.book_id == book_id and loan.member.member_id == member_id and loan.is_active:
                active_loan = loan
                break

        if not active_loan:
            raise LoanNotFoundError("No active loan found.")

        book.return_book()
        active_loan.close_loan()
        return f"{member.name} returned {book.title}"

    def view_books(self):
        return self._books.values()

    def view_members(self):
        return self._members.values()

    def view_loans(self):
        return self._loans
