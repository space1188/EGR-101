
import random as r

def main() :

    myFile = 'randomNumbers.txt'

    with open(myFile, 'w') as file:
        file.write(str(r.randint(0,9)))