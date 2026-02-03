
from typing import List, Dict
from collections import defaultdict
import datetime

class Expense:
    """
    Represents a single expense with amount, category, and date.
    """
    def __init__(self, amount: float, category: str, date: str = None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today().isoformat()

    def __str__(self):
        return f"{self.date} | {self.category} | ${self.amount:.2f}"

class ExpenseTracker:
    """
    Tracks expenses and provides analysis.
    """
    def __init__(self):
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense):
        """Add a new expense."""
        self.expenses.append(expense)
        print(f"[INFO] Added: {expense}")

    def remove_expense(self, index: int):
        """Remove expense by index."""
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"[INFO] Removed: {removed}")
        else:
            print("[ERROR] Invalid index.")

    def total_by_category(self) -> Dict[str, float]:
        """Return total spent per category."""
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e.category] += e.amount
        return dict(totals)

    def show_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("[INFO] No expenses recorded.")
            return
        print("\nIndex | Date       | Category | Amount")
        print("---------------------------------------")
        for idx, e in enumerate(self.expenses):
            print(f"{idx}     | {e}")

    def summary(self):
        """Show category-wise totals."""
        totals = self.total_by_category()
        if not totals:
            print("[INFO] No expenses to summarize.")
            return
        print("\nCategory-wise Totals:")
        print("----------------------")
        for cat, amt in totals.items():
            print(f"{cat}: ${amt:.2f}")

# ---------------------------
# INTERACTIVE MENU
# ---------------------------
def main():
    tracker = ExpenseTracker()
    print("=== Welcome to Smart Expense Tracker ===")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Show All Expenses")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ").strip()
                tracker.add_expense(Expense(amount, category))
            except ValueError:
                print("[ERROR] Invalid amount. Try again.")

        elif choice == "2":
            tracker.show_expenses()
            try:
                index = int(input("Enter index to remove: "))
                tracker.remove_expense(index)
            except ValueError:
                print("[ERROR] Invalid index. Try again.")

        elif choice == "3":
            tracker.show_expenses()

        elif choice == "4":
            tracker.summary()

        elif choice == "5":
            print("Exiting. Goodbye!")
            break

        else:
            print("[ERROR] Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()
