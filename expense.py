# expenses = [10.50, 8,5,15,20]
# sum = 0

# for x in expenses:
#     sum = sum + x

# print("You spent $", sum, "on lunch this week", sep='')

# total = sum(expenses)

total = 0 
expense = []
for i in range(7):
    expense.append(float(input("enter an expense:")))

total = sum(expense)

print("you spent $", total, sep="")
