# get the loan details

money_owed = float(input("How much money do you owe, in dollars?\n"))

apr = float(input("annual percentage\n"))
payment = float(input("monthly payment\n"))
months = float(input("how manymonths do you want to see results\n"))

#divide apr by 100 to make percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
# add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    # make payment
    money_owed = money_owed - payment

    #print the results
    print("paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("now I owe", money_owed)
