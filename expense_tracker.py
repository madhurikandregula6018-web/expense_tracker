# Expense Tracker

print("------ Expense Tracker ------")

num = int(input("How many expenses do you want to enter? "))

expenses = []

for i in range(num):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

total = sum(expenses)
highest = max(expenses)
lowest = min(expenses)
average = total / num

print("\n----- Expense Summary -----")
print("Total Expense:", total)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)
print("Average Expense:", average)