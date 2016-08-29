import random
import time
import sys

random.seed(time.localtime())


while True:
    print("\nNew game\n")
    myNumber = random.randint(1, 9)
    counter = 1

    while True:
        userInput = input("\nWhat is your guess? ")

        if userInput == "exit":
            sys.exit()

        userInput = int(userInput)

        if userInput == myNumber:
            print("Good guess. I was thinking of %d. You guessed %d times." % (myNumber, counter))
            break

        print("I was thinking ", "less" if myNumber < userInput else "more", ".")

        counter += 1
