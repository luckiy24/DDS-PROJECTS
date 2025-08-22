import json
from datetime import datetime

FILENAME = "transactions.json"

def load_transactions():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open(FILENAME, "w") as f:
        json.dump(transactions, f, indent=4)

def add_transaction(transactions):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    ttype = input("Enter type (Income/Expense): ").capitalize()
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")
    transaction = {
        "date": date,
        "category": category,
        "type": ttype,
        "amount": amount,
        "note": note
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Transaction added successfully!\n")

def view_transactions(transactions):
    if not transactions:
        print("No transactions found.\n")
        return
    print("\nAll Transactions:")
    for t in transactions:
        print(f"{t['date']} | {t['category']} | {t['type']} | {t['amount']} | {t['note']}")
    print()

def search_transactions(transactions):
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in transactions if keyword in t['note'].lower() or keyword in t['category'].lower()]
    if results:
        print("\nSearch Results:")
        for t in results:
            print(f"{t['date']} | {t['category']} | {t['type']} | {t['amount']} | {t['note']}")
    else:
        print("No matching transactions found.\n")

def filter_expenses(transactions):
    limit = float(input("Enter minimum expense amount: "))
    results = [t for t in transactions if t['type'] == "Expense" and t['amount'] > limit]
    if results:
        print("\nFiltered Expenses:")
        for t in results:
            print(f"{t['date']} | {t['category']} | {t['amount']} | {t['note']}")
    else:
        print("No expenses above this amount.\n")

def sort_transactions(transactions):
    print("1. Sort by Date")
    print("2. Sort by Amount")
    choice = input("Choose an option: ")
    if choice == "1":
        transactions.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"))
    elif choice == "2":
        transactions.sort(key=lambda x: x['amount'])
    view_transactions(transactions)

def monthly_summary(transactions):
    month = input("Enter month (YYYY-MM): ")
    total_income, total_expense = 0, 0
    for t in transactions:
        if t['date'].startswith(month):
            if t['type'] == "Income":
                total_income += t['amount']
            elif t['type'] == "Expense":
                total_expense += t['amount']
    print(f"\nSummary for {month}:")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Savings: {total_income - total_expense}\n")

def main():
    transactions = load_transactions()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Search Transactions")
        print("4. Filter Expenses")
        print("5. Sort Transactions")
        print("6. Monthly Summary")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            search_transactions(transactions)
        elif choice == "4":
            filter_expenses(transactions)
        elif choice == "5":
            sort_transactions(transactions)
        elif choice == "6":
            monthly_summary(transactions)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
