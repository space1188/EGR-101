# Brian Diosna hw4q5

import random

def hundredCoinToss(debug) :

    # establish head and tail amounts
    headAmount = 0
    tailAmount = 0

    # flip a coin 100 times
    for i in range(0, 100) :
        flip = random.randint(0, 1)
        if flip == 0 :
            headAmount += 1
        else :
            tailAmount += 1
    
    # prints useful stats if debug is 1
    if debug == 1 :
        print("Head amount: " + str(headAmount))
        print("Tail amount: " + str(tailAmount))

    # check to see if tail and head amounts are equal and return true or false
    if headAmount == tailAmount :
        return True
    else :
        return False

def main():

    # establish the starting amount of trials
    startingTrials = 10

    for i in range(0, 6) :

        totalSuccessTrials = 0

        # calculate the number of successes after x amount of trials
        for i in range(0, startingTrials):
            if hundredCoinToss(0) :
                totalSuccessTrials += 1
        
        # calculate the average success rate
        averageSuccess = totalSuccessTrials / startingTrials

        # print the results
        print("Trials : " + str(startingTrials) + " average success : " + str(averageSuccess))

        # multiply starting trials by 10
        startingTrials *= 10


if __name__ == "__main__" :
    main()
