# Brian Diosna hw4q4

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

    # toss the coin in debug mode
    print(hundredCoinToss(1))

    

if __name__ == "__main__" :
    main()
