# Brian Diosan

print("Enter a range of years to test.")

# ask the user to for a range of years and convert to int
firstYear = int(input("Enter the first year :"))
secondYear = int(input("Enter the second year :"))

# establish the list of leap years
leapYears = []

# loop through each year within the range and perform the calculations
for year in range(firstYear, secondYear + 1) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                leapYears.append(year)
        else :
            leapYears.append(year)


# print the results
print("Number of leap years in : " + str(len(leapYears)))
print(leapYears)