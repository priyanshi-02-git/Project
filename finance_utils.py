import json

# Global list to store transactions
transactions = []

def display_menu():
    print("\n--- Personal Finance Manager ---")
    print("1. Add a new transaction")
    print("2. View transactions")
    print("3. View summary")
    print("4. Search for a transaction")
    print("5. Save data to a file")
    print("6. Load data from a file")
    print("7. Exit")

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    type_ = input("Type (income/expense): ").lower()

    single_transaction = {
        'date': date,
        'description': description,
        'amount': amount,
        'type': type_
    }
    
    transactions.append(single_transaction)
    print("Transaction added successfully!")

def view_transactions():
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to view all: ")
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to view all: ")

    found = False
    print("\n--- Transaction List ---")
    for t in transactions:
        if start_date and end_date:
            if start_date <= t['date'] <= end_date:
                print(f"{t['date']} | {t['description']} | {t['amount']} | {t['type']}")
                found = True
        else:
            print(f"{t['date']} | {t['description']} | {t['amount']} | {t['type']}")
            found = True
    
    if not found:
        print("No transactions found.")

def view_summary():
    # Corrected logic: checking t['type'], not ['type']
    total_income = sum(t['amount'] for t in transactions if t['type'] == "income")
    total_expense = sum(t['amount'] for t in transactions if t['type'] == "expense")
    total_savings = total_income - total_expense

    print("\n--- Summary ---")
    print(f"Total Income : {total_income}/-")
    print(f"Total Expense: {total_expense}/-")
    print(f"Net Savings  : {total_savings}/-")

def search_transactions():
    user_input = input("Enter description or amount to search: ").lower()
    found = False

    print("\n--- Search Results ---")
    for t in transactions:
        # Convert amount to string to search properly
        if user_input in t['description'].lower() or user_input in str(t['amount']):
            print(f"{t['date']} | {t['description']} | {t['amount']} | {t['type']}")
            found = True

    if not found:
        print("No transaction found matching that criteria.")

# These functions must be un-indented (outside of search_transactions)
def save_data():
    file_name = input("Enter the name of file to save (e.g., data.json): ")
    try:
        # Use 'w' (write) mode, not 'a' (append), to create valid JSON
        with open(file_name, 'w') as file:
            json.dump(transactions, file, indent=4)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_data():
    file_name = input("Enter the filename to load data: ")
    global transactions
    try:
        with open(file_name, 'r') as file:
            transactions = json.load(file)
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error reading the file format.")