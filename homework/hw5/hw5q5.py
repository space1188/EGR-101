# Brian Diosan hw5q4

import random
from tracemalloc import start

import matplotlib.pyplot as plt
import numpy as npcle

import time

# this function will determine if a given list of numbers is consecutive
def isConsecutive(list) :
    # establish the result variable
    result = True
    # loop for each item in the list
    for i in range(len(list)-1) :
        currNum = list[i]
        # check if the number after the current number is the same number plus 1 (which means its consecutive)
        if list[i+1] != (currNum+1) :
            result = False
    # print the result
    return result


# define the ace location function
def playHand():
    
    # create a shuffled deck
    shuffleDeck = random.sample(range(52), 52)

    hasPerfectBridge = False

    # deal 13 cards to each player
    player1 = shuffleDeck[0:13]
    player2 = shuffleDeck[13:26]
    player3 = shuffleDeck[26:39]
    player4 = shuffleDeck[39:52]
    
    # now sort them to make it easier to determine if its perfect or not
    player1.sort();
    player2.sort();
    player3.sort();
    player4.sort();
    
    # check if any of the player have any consecutive cards because if they do then that means its a perfect bridge in a particular suit
    # ALSO, the starting number must start with an ace, those are located at 0, 13, 26 and 39
    if isConsecutive(player1) and (player1[0] == 0 or player1[0] == 13 or player1[0] == 26 or player1[0] == 39) :
        hasPerfectBridge = True

    # return the result (true or false)
    return hasPerfectBridge


def main() :

    # establish the starting amount of trials
    numberOfTrials = 10

    # establish x and y plotting point values for the graph
    xVals = []
    yVals = []

    for z in range(0, 7) :

        # for each round of trails, establish vars that will hold data for the average
        totalAmount = 0

        # get the starting time
        startingTime = time.time()

        # play x amount of hands and record the amount of perfect bridges
        for i in range(0, numberOfTrials):
            if playHand() :
                totalAmount += 1

        # get the ending time
        endingTime = time.time()
        
        # get the time it took to finish the simulation with x amount of trials
        timeToFinish = (endingTime - startingTime)

        # print some useful progress data
        print("Number of hands playerd : " + str(numberOfTrials) + " in : " + str(timeToFinish) + " sec")

        # append the values/plotting points to the list
        xVals.append(numberOfTrials)
        yVals.append(timeToFinish)


        numberOfTrials *= 10
    

    # graph the points with matplotlib
    fig, ax = plt.subplots()
    ax.plot(xVals, yVals)

    ax.set(xlabel='# of Hands', ylabel='Time to deal bridge hand (sec)',
        title='EGR-101 (hw5q5)')
    ax.grid()

    fig.savefig("test.png")
    plt.show()


if __name__ == "__main__" :
    main()