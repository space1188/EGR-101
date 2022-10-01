
# Brian Diosan hw5q3

import random

import matplotlib.pyplot as plt
import numpy as npcle

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
    numberOfTrials = 100000

    # establish x and y plotting point values for the graph
    xVals = []
    yVals = []

    # loop for each coupon amount (3 through 20)
    for z in range(3, 21) :

        # for each round of trails, establish vars that will hold data for the average
        totalAmount = 0
        averageBoxes = 0

        # for the current coupon amount, get the average after 100k trials
        for i in range(0, numberOfTrials):
            trials = couponTrials(z, False)
            totalAmount += trials
        
        # calculate the average amount of boxes to get all coupons
        averageBoxes = totalAmount / numberOfTrials

        # append the values/plotting points to the list
        xVals.append(z)
        yVals.append(averageBoxes)
        # print the results just to see how the simulation progress is going because it takes a while
        print("Number of coupons " + str(z) + ", average: " + str(averageBoxes))
    

    # graph the points with matplotlib
    fig, ax = plt.subplots()
    ax.plot(xVals, yVals)

    ax.set(xlabel='# Of Coupons', ylabel='Average amount of boxes',
        title='Simulation with 100k trials (hw5q3)')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

        

if __name__ == "__main__" :
    main()


