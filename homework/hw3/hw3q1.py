# Brian Diosan

# ask the user to enter a number to test
number = int(input("Enter a number: "))

# establish a list if divisors for that number
divisors = []

# calculate the divisors and append to the list
for i in range(1, number + 1) :
    if number % i == 0 and i != 1 :
            divisors.append(i)

# establish a list for the prime divisors
primeNums = []

# loop through each divisor to perform calculations
for i in range(0, len(divisors)) :

    # set the current selected number
    currNum = divisors[i]

    # establish a list that will hold all the factors for the selected number
    currentFactors = []

    # calculate if the number is prime
    for num in range(1, currNum) :
        if currNum % num == 0 :
            currentFactors.append(num)

    # if the number is prime then append to the primeNums list
    if len(currentFactors) < 2 :
        primeNums.append(currNum)
    

# print the results
print("The prime factors of " + str(number) + " are ")
print(primeNums)