# Brian Diosna hw4q3

import random

# establish the ace number constants
aceNumbers = [0, 13, 26, 39]

# define the ace location function
def aceLocation(debug):
    # create a shuffled deck
    shuffleDeck = random.sample(range(52), 52)

    aceLocations = []

    # if debug == 1 then show debug info
    if debug == 1 :
        print(shuffleDeck)

        # loop through each card and capture the locations of the aces
        for i in range(0, len(shuffleDeck)) :
            if shuffleDeck[i] in aceNumbers :
                aceLocations.append(i)

        # print the ace locations
        print(aceLocations)
        aceLocations.sort
        # print the sorted ace locations
        print(aceLocations)
        # print the first ace location
        return aceLocations[0]

    else :
         # loop through each card and capture the locations of the aces
        for i in range(0, len(shuffleDeck)) :
            if shuffleDeck[i] in aceNumbers :
                aceLocations.append(i)

        # print the first ace location
        return aceLocations[0]

def main():

    # establish the starting amount of trials
    startingTrials = 10

    for i in range(0, 6) :

        totalAmount = 0
        averageAceLocation = 0

        # calculate the first ace location x amount of times
        for i in range(0, startingTrials):
            aceLoc = aceLocation(0)
            totalAmount += aceLoc
        
        # calculate the average location
        averageAceLocation = totalAmount / startingTrials

        # print the results
        print("Trials : " + str(startingTrials) + " average location of first ace : " + str(averageAceLocation))

        # multiply starting trials by 10
        startingTrials *= 10

        

if __name__ == "__main__" :
    main()
