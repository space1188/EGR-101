# Brian Diosan hw3q2

# establish a list that contains the number of elements
numOfElem = 0

# establish the list the will contain all the user inputted elements
list = []

# ask the user to enter numbers twice
for i in range(0, 2) :
    numOfElem = int(input("Enter number of elements: "))
    for i in range(0, numOfElem) :
        list.append(int(input("Enter element: ")))

# establish a boolean that will determine if it is sorted or not
isSorted = False

# loop forever until it is sorted
while isSorted != True :
    # loop through each element in the list to see which ones are greater than the previous elements, if so, then swap them.
    for i in range(0, len(list) - 1) :
        currNum = list[i]
        nextNum = list[i + 1]

        if currNum > nextNum :
            list[i] = nextNum
            list[i+1] = currNum

    notSorted = True

    # check if it is sorted or not
    for i in range(0, len(list) - 1) :
        currNum = list[i]
        nextNum = list[i + 1]

        if currNum > nextNum :
            notSorted = False

    # if it is sorted, then break out of the while loop because we are done
    if notSorted :
        isSorted = True
    

# print the sorted list
print(list)
