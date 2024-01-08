def add_expenses(expenses, amount, category):
  expenses.append({"amount": amount, "expenses": expenses})

expenses = []


def princ_expenses(expenses):
  for expense in expenses:
    print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
  pass

print("Expenses: ")
print(expenses)