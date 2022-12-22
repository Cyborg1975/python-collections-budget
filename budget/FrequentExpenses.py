import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses = open("../data/spending_data.csv", "r")

spending_categories = []

for expense in expenses.list:
    expense.category.append(spending_categories)

spending_counter = collections.Counter(spending_categories)

print(spending_counter)

top5 = spending_counter.most_common(5)

zip("categories", "values", *top5)

fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
