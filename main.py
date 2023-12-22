from datetime import datetime
from uuid import uuid4

class Expense:
    def __init__(self, title, amount):
        self.id = uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update(self, new_title=None, new_amount=None):
        if new_title:
            self.title = new_title
        if new_amount:
            self.amount = new_amount
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return {"expenses": [expense.to_dict() for expense in self.expenses]}

# Example usage
expense1 = Expense("Groceries", 100)
expense2 = Expense("Utilities", 50)

db = ExpenseDB()
db.add_expense(expense1)
db.add_expense(expense2)

# Update an expense
expense1.update(new_amount=120)

# Retrieve an expense by ID and print it
expense_by_id = db.get_expense_by_id(1)
if expense_by_id:
    print(expense_by_id.to_dict())

# Retrieve expenses by title and print them
expenses_by_title = db.get_expenses_by_title("Utilities")
for expense in expenses_by_title:
    print(expense.to_dict())

# Remove an expense
db.remove_expense(2)

# Convert database to dictionary and print it
print(db.to_dict())
