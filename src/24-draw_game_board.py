_MAX_DIMENSION = 50

import sys

def get_dimension():
    """Asks the user for a dimension and andles bad input."""

    inp = input("\nEnter the single digit dimension (i.e.: 3 for a 3x3 board): ")

    # Input must be digit
    if not inp.isdigit():
        sys.exit("Bad input.")

    # Convert string to int
    inp = int(inp)

    # Sanity check
    if inp > _MAX_DIMENSION:
        if input("(%dx%d) is such a large dimension. Are you sure? (y/n): " % (inp, inp)) != 'y':
            sys.exit()

    return inp


def print_horizontal(dim):
    """Prints one horizontal line for the game."""
    print (" ---" * dim)

def print_vertical(dim):
    """Prints one vertical line for the game."""

    # print all but the last '|' without newline
    print("|   " * dim, end="")

    # print the last '|' with a newline
    print("|")

def print_board(dim):

    # Print the board without the closing horizontal lines - to avoid duplication
    for i in range(dim):
        print_horizontal(dim)
        print_vertical(dim)

    # Then print the last closing horizontal line
    print_horizontal(dim)

if __name__ == "__main__":

    print_board(get_dimension())