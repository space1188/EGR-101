# Brian Diosan

# ask the user to enter a year and convert to int
year = int(input("Enter the year to test :"))

# establish the answer boolean variable
answer = False

# perform the calculations and change the answer accordingly
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            answer = True
    else :
        answer = True

# print the result
if answer :
    print("The year " + str(year) + " is a leap year")
else :
    print("The year " + str(year) + " is not a leap year")