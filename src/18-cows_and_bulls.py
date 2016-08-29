###########
# Imports #
###########
import random
import time
import sys

###########
# Helpers #
###########

DEBUG = False
HELP = False

def _debug(msg):
    if DEBUG: print("[DEBUG] " + msg)

def _help(msg):
    if HELP: print("[HELP] " + msg)



#########################
# Seed random generator #
#########################
random.seed(time.localtime())

def get_digit():
    "Return a random single digit number"
    return random.randint(0,9)

def get_user_input():
    "Handles user input, checks for quit request and illegal format."
    guess = input("\nGuess the number ('q' for quit): ")

    # Handle quit request
    if guess == 'q':
        sys.exit()

    # Check for illegal arguments
    if len(guess) != 4 or not guess.isdigit(): raise ValueError

    # Create and return a List from the input String
    guessList = []
    for digit in guess:
        guessList.append(int(digit))
    return guessList


class Game(object):
    "Object representing a single game from beginning to end."
    def __init__(self):
        self.solution = (get_digit(), get_digit(), get_digit(), get_digit())    # Storing the as a tuple of digits
        self.solutionStr = "".join(map(str, self.solution))                 # And also as a string for easier printing
        self.iterations = []                                          # Store all GameIterations for final analysis

    def final_report(self):
        "Display the final report with details for each guess and the number of guesses"
        print("\nCongratulations! You win!\n")
        counter = 0
        for iteration in self.iterations:
            print(repr(iteration))
            counter += 1
        print("\nIt took you %d guesses to solve the problem." % counter)

    def play(self):
        "A single play of the game."
        PLAY = True

        while PLAY:
            try:
                iteration = GameIteration(get_user_input(), self.solution)
                PLAY = iteration.evaluate()             # If game was won, PLAY is set to False.
                self.iterations.append(iteration)       # Store this iteration in List for final report.
            # User requested to quit the game
            except SystemExit:
                print("Thanks for playing! You requested to quit the game. Bye!")
                raise
            # User entered bad value
            except ValueError:
                print("Bad input")
                continue

        # Game ended, print report.
        self.final_report()


class GameIteration(object):
    "Object representing a single iteration (a new guess) of the game."
    def __init__(self, guessedNumber, solution):

        self.guessedNumber = guessedNumber
        self.guessedNumStr = "".join(map(str, guessedNumber))       # Printing helper

        self.solution = solution
        self.solutionStr = "".join(map(str, solution))              # Printing helper

        self.numOfCows = 0
        self.numOfBulls = 0


    def __repr__(self):
        return "<guessedNumber='%s', solution='%s', numOfCows='%d', numOfBulls='%d'>" \
               % (self.guessedNumStr, self.solutionStr, self.numOfCows, self.numOfBulls)

    def check_cows(self, guess):
        "Number of cows is the number of correct digits at the right index."
        numOfCows = 0
        for guessDigit, solutionDigit in zip(guess, self.solution):
            _debug("Guess: %d, solution: %d" % (guessDigit, solutionDigit))
            if guessDigit == solutionDigit:
                numOfCows += 1
                _debug("Found a cow. Num of cows: %d" % numOfCows)
        return numOfCows

    def check_bulls(self, guess):
        "Number of bulls are the number of correct digits at the wrong index"
        numOfBulls = 0
        for solutionDigit in self.solution:
            _debug("Guess: %d" % solutionDigit)
            if solutionDigit in guess:
                numOfBulls += 1
                _debug("Found a Bull. Num of bulls: %d" % (numOfBulls - self.numOfCows))     # Cows are not counted in bulls.
        return numOfBulls

    def evaluate(self):
        "Check the guess, print number of cows and bulls, and decide if the guess was correct."
        self.numOfCows = self.check_cows(self.guessedNumber)

        # TODO; understand why the double substraction gives correct result
        self.numOfBulls = self.check_bulls(self.guessedNumber) - self.numOfCows

        _help("solution is " + ''.join(map(str, self.solution)))
        _help(repr(self))

        print("\nYou have %d cows and %d bulls" % (self.numOfCows, self.numOfBulls))        # Report latest status.

        return False if self.numOfCows == 4 else True       # check for win.




if __name__ == "__main__":
    # Run game until the user requests to quit
    while True:
        Game().play()       # Start a new game after every win.
        if input("\nWould you like to play again? (y/n): ") != 'y': sys.exit()