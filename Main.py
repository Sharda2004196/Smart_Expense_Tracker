from typing import List, Dict
from collections import defaultdict
import datetime

class Expense:
    """Class representing a single expense."""
    def __init__(self, amount: float, category: str, date: str = None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today().isoformat()

class ExpenseTracker:
    """Class to track and analyze expenses."""
    def __init__(self):
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, index: int):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    def total_by_category(self) -> Dict[str, float]:
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e.category] += e.amount
        return dict(totals)

    def summary(self):
        print("Expense Summary:")
        totals = self.total_by_category()
        for cat, amt in totals.items():
            print(f"{cat}: ${amt:.2f}")

# Usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(Expense(50, "Food"))
    tracker.add_expense(Expense(20, "Transport"))
    tracker.add_expense(Expense(30, "Food"))
    tracker.summary()
