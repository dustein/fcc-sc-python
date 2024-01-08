def add_expenses(expenses, amount, category):
  expenses.append({"amount": amount, "expenses": expenses})

expenses = []


def princ_expenses(expenses):
  for expense in expenses:
    print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
  return sum(map(lambda expense : expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
  return filter(lambda expense : expense['category'] == category, expenses)

def main():
  expenses = []
  while True:
    print('\nExpense Tracker')
    print('1. Add an expense')
    print('2. List all expenses')
    print('3. Show total expenses')
    print('4. Filter expenses by category')
    print('5. Exit')
        
    choice = input('Enter your choice: ')
    if choice == '1':
      amount = float(input('Enter amount: '))
      category = input('Enter category: ')
      add_expenses(expenses, amount, category)
      
# teste = lambda x : x * 2
# print(sum(map(teste, [2, 3, 5, 8])))

print("Expenses: ")
print(expenses)