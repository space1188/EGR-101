# Brian Diosan


# ask the user to enter a value for n
nValue = int(input("Enter N:"))

# establish the list that contains the new balances per compounding period
valueEachCompound = []

# estsablish the initial balance amount
currentBalance = 1.00

# loop for each compounding period
for i in range(0, nValue) :
    # perform the compound calculation
    valueEachCompound.append((1+1/(2**i))**(2**i))

# print the results
print(valueEachCompound)

