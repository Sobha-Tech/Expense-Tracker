expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, etc): ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("✅ Expense added!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n📋 Expense List:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']}, Category: {expense['category']}")
    print()


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"💰 Total Expense: {total}\n")


def menu():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice\n")


menu()