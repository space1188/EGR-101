# Brian Diosn - in class three

# define the list that will contain the user inputted numbers
listOfNums = []

# ask the user how many numbers he/she wants to enter
totalNums = int(input("Enter number of elements:"))

# loop through each number and ask the user for input
for i in range(1, totalNums+1) :
    value = int(input("Enter element:"))
    listOfNums.append(value)

# sort the list from smallest to largest
listOfNums.sort()

# print the second to last value
print("Second largest element is:", listOfNums[totalNums-2])
