# Brian Diosan hw3q4

# ask the user to enter number of K terms
numberOfTerms = int(input("N: "))

total = 0.0

exactPi = 3.141592653589793

# loop starting at numberOfTerms given from user
for i in range(0, numberOfTerms) :

    # apply the formula given in the summation notation
    appFormVal = float((2 * (-1 ** i) * (3 ** (0.5 - i)))/(2 * i + 1))
    # add it to total
    total += appFormVal

# print the results

print("Calculated value of pi: " + str(total))
print("Error: " + str(exactPi - total))