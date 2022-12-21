from . import Expense
import collections

expenses = Expense.Expenses()

expenses.read_expenses(data/spending_data.csv)

spending_categories = []

for expense in expenses.list():
    expense.category.append(spending_categories)


spending_counter = collections.Counter(spending_categories)

print(spending_counter)
