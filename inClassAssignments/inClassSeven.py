
# Brian Diosan in class seveb

# retrieve user inputted values
monthlySavingAmount = float(input('Enter how much you plan to save each month : '))
goalAmount = float(input("Enter your end goal amount : "))

# establish interest rate
rate = 0.07/12

total = 0
n = 0

# loop as long as total is less than the goal amount
while total < goalAmount :
    # apply interest
    interest = total * rate
    # add it to the total
    total += monthlySavingAmount + interest
    # add to months amount
    n += 1

# print the result
print('After ' + str(n) + " months you will have: $" + str(round(total*100) / 100))

