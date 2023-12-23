# Expense Tracker Documentation
This documentation provides an overview of the classes and functions in the provided Python code for an Expense Tracker found in isaac_final.py file as my final project for AltSchoolAfrica first semester. The code defines two classes, Expense and ExpenseDB, to manage and store information about expenses.

# Expense Class
## 'Expense' Class
The Expense class represents an individual expense with the following attributes:

- id: A unique identifier generated using the uuid4 module.
- title: A string representing the title or description of the expense.
- amount: A numerical value representing the expense amount.
- created_at: A datetime object indicating the creation timestamp of the expense.
- updated_at: A datetime object indicating the last update timestamp of the expense.

### Methods:
```__init__(self, title, amount)```
Initializes a new instance of the Expense class.
- **Parameters:**
    - title: The title or description of the expense.
    - amount: The numerical value representing the expense amount.

```update(self, new_title=None, new_amount=None)```
Updates the expense with new information.

- **Parameters:**
    - new_title: New title for the expense (default is None).
    - new_amount: New amount for the expense (default is None).

```to_dict(self)```
Converts the expense object to a dictionary for easy serialization.
Returns a dictionary containing the expense details.

# ExpenseDB Class
## ExpenseDB Class

The ExpenseDB class represents a simple expense database that stores a collection of Expense objects.

### Methods:
```__init__(self)```
Initializes a new instance of the ExpenseDB class with an empty list of expenses.

```add_expense(self, expense)```
Adds a new expense to the database.

- **Parameters:**
    - expense: An instance of the Expense class to be added to the database.

```remove_expense(self, expense_id)```
Removes an expense from the database based on its unique identifier.
- **Parameters:**
    - expense_id: The unique identifier of the expense to be removed.

```get_expense_by_id(self, expense_id)```
Retrieves an expense from the database based on its unique identifier.

- **Parameters:**
  - expense_id: The unique identifier of the desired expense.
    - Returns: The Expense object if found, or None if not found.

```get_expenses_by_title(self, title)```
Retrieves a list of expenses from the database based on their title.

- **Parameters:**
    - title: The title or description of the expenses to be retrieved.
      - Returns: A list of Expense objects with matching titles.

```to_dict(self)```
- Converts the entire database to a dictionary for easy serialization.
- Returns a dictionary containing a list of dictionaries representing each expense.

## Example Usage
The code concludes with an example of how to use the defined classes:

- Creating two Expense objects (expense1 and expense2).
- Creating an ExpenseDB object (db).
- Adding expenses to the database.
- Updating an expense (expense1).
- Retrieving and printing an expense by ID.
- Retrieving and printing expenses by title.
- Removing an expense from the database.
- Converting the entire database to a dictionary and printing it.


# Cloning the Expense Tracker Repository
To clone the Expense Tracker repository on GitHub, follow these steps:

1. Copy Repository URL:
    - Visit the GitHub repository page containing the Expense Tracker code.
    - Click on the "Code" button, and copy the repository URL (HTTPS or SSH).

2. Open Terminal (Linux/Mac) or Command Prompt (Windows):
    - Navigate to the directory where you want to clone the repository.

3. Clone the Repository:
    - Use the git clone command followed by the copied repository URL:
    - ```git clone <repository_url>```
    - Replace <repository_url> with the URL you copied.

4. Navigate to the Cloned Directory:
    - Change into the cloned directory:
    - ```cd final_project```
    - Now, you have successfully cloned the repository to your local machine.

# Running the Expense Tracker Code

To run the Expense Tracker code, follow these steps:

1. Ensure Python is Installed:
    - Make sure Python is installed on your machine. You can download it from python.org.

2. Install Dependencies (Optional):
    - If the uuid module is not available in your Python installation, you might need to install it. However, in most cases, it's included in the standard library.
    - ```pip install uuid```

3. Run the Code:
    - Open a terminal or command prompt in the cloned directory.
    - Run the script using the Python interpreter:
    - ```python isaac_final.py```
    - If you're using Python 3, you might need to use python3 instead of python. Review Output:

The script includes example usage at the end, which demonstrates creating expenses, updating them, retrieving by ID or title, removing an expense, and converting the database to a dictionary.

