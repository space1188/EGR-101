# Brian Diosan hw4q1

import random

# establish the variable that will hold the lowest score
lowestScore = -1

numberToGuess = 0

# print the banner
def gameBanner() :
    print("Guessing Game Computer Program")

# print the intro
def introDisplay() :
    return int(input("Guess a number between 1 and 30: "))

def main():

    gameBanner()
    lowestScore = -1

    # loop forever until the user doesnt want to play anymore
    while input("Do you want to play the game (y/n)? ") == "y" :
        
        # generate a random number to guess
        numberToGuess = random.randint(1, 30)
        # ask the user to guess
        guess = introDisplay()
        currentAttempts = 0

        # keep asking until the user guesses the right number
        while guess != numberToGuess :

            if guess > numberToGuess :
                print("Lower")
                currentAttempts += 1
            elif guess < numberToGuess:
                print("Higher")
                currentAttempts += 1

            guess = introDisplay()

        # tell the user he/she got it right and tell them the number of attempts
        currentAttempts += 1
        print("You guessed it!")
        print("Number of attempts: " + str(currentAttempts))

        # calculate if he got a lower score this time compared to the previous rounds
        if lowestScore < 0 :
            lowestScore = currentAttempts
        elif currentAttempts < lowestScore :
            lowestScore = currentAttempts

    # at the end of the game tell the user what his or her lowest score was
    print("Your lowest score for the session was " + str(lowestScore))

if __name__ == "__main__" :
    main()