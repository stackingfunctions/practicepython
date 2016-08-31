_DEBUG = False

import sys

def _debug(msg):
    if _DEBUG: print("[DEBUG] " + msg)

def get_user_answer(num):
    """Ask for user input. Only accepted values are 'c', 'l', 'm'"""

    # get the user input
    inp = input("I guess %d. If I guessed correctly, please enter 'c', if your number is less, enter 'l', dif it is more then enter 'm'" % num)
    _debug("inp: " + inp)

    # Check if input is legal
    while True:
        # Bad input
        if inp.strip() != 'c' and inp != 'l' and inp != 'm':
            print("Bad input.")
            inp = input("I guess %d. If I guessed correctly, please enter 'c', if your number is less, enter 'l', if it is more then enter 'm'" % num)
            _debug("Bad input. new inp: " + inp)

        # Correct input
        else:
            _debug("Correct input.")
            break

    return inp.strip()

def evaluate_answer(inp, available_numbers):
    """Evaluates if the pick was correct, less, or more.
    It returns None in case of correct pick and the appropriate half of the List"""

    # Determine the middle point
    midindex = len(available_numbers) // 2

    # Correct answer - return None
    if inp == 'c':
        return None

    # User picked a number that is less - return first half of list
    elif inp == 'l':
        return available_numbers[:midindex]

    # User picked a number that is more - return second half of list
    elif inp == 'm':
        return available_numbers[midindex + 1:]

    # Execution should never get here
    else:
        sys.exit("I suck! Quiting ...")

def guess(available_numbers):
    """Makes guesses in a recursive fassion until it exhausts all possibilities of guesses the picked number."""

    _debug("available_numbers[]: " + ",".join(map(str, available_numbers)))

    # Increment the global counter of iterations so at the end it can be reported
    global _num_of_iterations
    _num_of_iterations += 1
    _debug("_num_of_iterations: " + str(_num_of_iterations))

    # Store the length of the list because it will be reused
    listlen = len(available_numbers)
    _debug("listlen: " + str(listlen))

    # No more available numbers to pick from. User either made a mistake somewhere or lied.
    if listlen == 0:
        _debug("listlen == 0")
        sys.exit("Something is seriously wrong. Did you lie to me?")

    # There is only 1 more available number. Pick that for next.
    elif listlen == 1:
        middle_index = 0
        next_pick = available_numbers[0]
        _debug("listlen == 1 - next_pick: " + str(next_pick))

    # There are still multiple available numbers
    else:

        # Find the middle of the values and it's index
        middle_index = listlen // 2
        next_pick = available_numbers[middle_index]
        _debug("else - middle_index: %d - next_pick: %d" % (middle_index, next_pick))

    # Ask the user about my next pick
    ans = get_user_answer(available_numbers[middle_index])
    _debug("ans:" + ans)

    # Evaluate user answer
    result = evaluate_answer(ans, available_numbers)

    # Solution was found - return it
    if result == None:
        _debug("Found solution: " + str(next_pick))
        return next_pick

    _debug("result: " + ",".join(map(str, result)))

    # We still dont know the answer and have available numbers to pick from. Recursive call.
    return guess(result)

def play_game():

    # Intro
    print("Please pick a number between 0 and 100 and don't tell me. I will guess the number.")

    # Create global variable to count iterations
    global _num_of_iterations
    _num_of_iterations = 0

    # Guess until we find the answer
    result = guess(list(range(100)))

    # Report result
    print("\nI guessed %d times to find out that you picked %d." % (_num_of_iterations, result))


if __name__ == "__main__":

    play_game()