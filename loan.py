class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True

    def close_loan(self):
        self.is_active = False
