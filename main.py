from library_service import LibraryService
from exceptions import *

def main():
    service = LibraryService()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            msg = service.add_book(book_id, title, author)
            print(msg)

        elif choice == "2":
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")
            msg = service.register_member(member_id, name, email)
            print(msg)

        elif choice == "3":
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            try:
                msg = service.borrow_book(book_id, member_id)
                print(msg)
            except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
                print("Error:", e)

        elif choice == "4":
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            try:
                msg = service.return_book(book_id, member_id)
                print(msg)
            except (BookNotFoundError, MemberNotFoundError, LoanNotFoundError) as e:
                print("Error:", e)

        elif choice == "5":
            books = service.view_books()
            if not books:
                print("No books found.")
            else:
                print("\n--- Books ---")
                for book in books:
                    status = "Available" if book.available else "Borrowed"
                    print(f"{book.book_id} - {book.title} by {book.author} [{status}]")

        elif choice == "6":
            members = service.view_members()
            if not members:
                print("No members found.")
            else:
                print("\n--- Members ---")
                for member in members:
                    print(f"{member.member_id} - {member.name} ({member.email})")

        elif choice == "7":
            loans = service.view_loans()
            if not loans:
                print("No loans found.")
            else:
                print("\n--- Loans ---")
                for loan in loans:
                    status = "Active" if loan.is_active else "Closed"
                    print(f"Loan {loan.loan_id}: {loan.member.name} | {loan.book.title} [{status}]")

        elif choice == "8":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
