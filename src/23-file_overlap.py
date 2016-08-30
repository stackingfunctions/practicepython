_FILE_1 = "../tmp/23/primenumbers.txt"
_FILE_2 = "../tmp/23/happynumbers.txt"


def read_numbers(file, list):
    """Read all numbers contained in the file"""
    with open(file, "r") as f1:
        line = f1.readline()
        while line:
            list.append(int(line.strip()))
            line = f1.readline()


def get_intersection():
    """Read both files and return a sorted list containing the intersection of the two sets of numbers"""

    # Create containers for the two types of numbers
    prime_numbers = []
    happy_numbers = []

    # Read both types of numbers
    read_numbers(_FILE_1, prime_numbers)
    read_numbers(_FILE_2, happy_numbers)

    # Get the intersection
    intersection = list(set(prime_numbers).intersection(set(happy_numbers)))

    # Another interesting solution is with list comprehension
    # Howeret it's performance is worse than the solution with sets - O(n**2)
    #
    #intersection = [element for element in prime_numbers if element in happy_numbers]

    # Be nice and sort it for better readability
    intersection.sort()

    return intersection

if __name__ == "__main__":

    print("The numbers under 1000, that are both prime and happy are: " + ", ".join(map(str, get_intersection())))