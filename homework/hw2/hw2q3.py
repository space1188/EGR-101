# Brian Diosan

# ask the user to enter an integer
number = int(input("Enter an integer :"))

# establish the resulting list
divisors = []

# loop through each number to see if its divisible
for num in range(1, number + 1) :
    if number % num == 0 :
        divisors.append(num)

# print the results
print(divisors)
print("The number of divisors for " + str(number) + " is " + str(len(divisors)))