
# Brian Diosan - in class nine

import random

# create the dice class
class Dicetoss :

    def __init__(self):
        self.upperside = 1

    # change the upperside to a random number 1-6
    def tossing(self):
        self.upperside = random.randint(1,6)
    
    # return the upperside to be used for whatever reason
    def get_upperside(self):
        return(self.upperside)

def main():

    # declare the number of rolls
    rolls = 4

    # tell the user how many rolls the application will perform
    print("Dice Toss " + str(rolls) + " Times With Two Dice")
    print("\n")

    # instantiate the two dice
    firstDie = Dicetoss()
    secondDie = Dicetoss()

    # roll the dice x amount of times
    for i in range(0, rolls) :
        # roll both of the dice
        firstDie.tossing()
        secondDie.tossing()
        # print the results
        print("First Die :" + str(firstDie.get_upperside()))
        print("Second Die :" + str(secondDie.get_upperside()))
        print("\n")

    print("Dice rolls are done")

main()