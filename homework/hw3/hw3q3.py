# Brian Diosan hw3q3

# ask the user to enter number of K terms
numberOfTerms = int(input("Enter number of K terms to compute: "))

total = 0.0

# loop starting at numberOfTerms given from user
for i in range(0, numberOfTerms) :

    # apply the formula given in the summation notation
    appFormVal = float((2 * (-1 ** i) * (3 ** (0.5 - i)))/(2 * i + 1))
    # add it to total
    total += appFormVal

# print the results
print(total)
