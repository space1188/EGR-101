# Brian Diosan


# ask the user to enter two integers as a range
firstNum = int(input("Enter a first number :"))
secondNum = int(input("Enter a second number :"))

# establish variable to hold the total
numOfNonPrime = 0

# loop through the range of numbers
for i in range(firstNum, secondNum + 1) :

    # establish the resulting list
    divisors = []

    # loop through each number to see if its divisible
    for num in range(1, i + 1) :
        if i % num == 0 :
            divisors.append(num)

    if len(divisors) > 2 :
        # if there are more than two divisors then it is not prime so add 1 to the total
        numOfNonPrime += 1



# print the results
print("The number of non prime numbers is " + str(numOfNonPrime))