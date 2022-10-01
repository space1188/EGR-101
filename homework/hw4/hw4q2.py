# Brian Diosna hw4q2

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


if __name__ == "__main__" :
    print(aceLocation(1))
