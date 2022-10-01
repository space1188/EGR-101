
# Brian Diosan hw5q2

import random

# define the coupon trials function which takes two parameters
def couponTrials(N, debug) :

    # establish the initial vars which will be utilized
    totalTrials = 0
    foundCoupons = []

    # fill the initial foundCoupons list with 0's
    for i in range(N) :
        foundCoupons.append(0)
    
    # now just loop forver until there are no mroe 0's in the foundCoupons list
    while 0 in foundCoupons :
        # generate a random number which will be our found coupon
        foundCoupon = random.randint(0, N-1)
        # add it to our foundCoupons list if it hasn't been added already
        foundCoupons[foundCoupon] = 1
        # add 1 to the trial amount
        totalTrials = totalTrials + 1

        # print some debug stats if debug == True
        if debug :
            print("Coupon " + str(foundCoupon) + " found in the box \nList of coupons found")
            print(foundCoupons)

    # more debug stats
    if debug :
        print("The number of boxes to obtains all coupons")
    # print the totalTrials result!
    return totalTrials


def main() :

    # establish the starting amount of trials
    startingTrials = 10

    for i in range(0, 6) :

        # for each round of trails, establish vars that will hold data for the average
        totalAmount = 0
        averageBoxes = 0

        # calculate the numbre of trials x amount of times
        for i in range(0, startingTrials):
            trials = couponTrials(5, False)
            totalAmount += trials
        
        # calculate the average amount of boxes to get all coupons
        averageBoxes = totalAmount / startingTrials

        # print the results
        print("Trials : " + str(startingTrials) + " average number of boxes : " + str(averageBoxes))

        # multiply starting trials by 10
        startingTrials *= 10
        

if __name__ == "__main__" :
    main()


