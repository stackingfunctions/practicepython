_DEBUG = False
_LIST_SIZE = 100
_LARGEST_NUMBER_IN_LIST = 100

def _debug(msg):
    if _DEBUG: print("[DEBUG] " + msg)



import random
import time
import sys


def getRandomIntList():
    """Generate a random length List containing random numbers.
    Length of the list can be set by _LIST_SIZE, and max value for the numbers can be set by _LARGEST_NUMBER_IN_LIST
    variables at the top of the file."""
    random.seed(time.localtime())
    newList = []
    for len in range(random.randint(6,_LIST_SIZE)):
        newList.append(random.randint(1, _LARGEST_NUMBER_IN_LIST))
    return newList

def _createGlobalCounter():
    """Creates a global counter called _counter and sets the value to 0."""
    global _counter
    _counter = 0

def doBinarySearch(numberToFind, unsortedList):
    """Sort the list before calling binarySearch() and create a global counter"""
    unsortedList.sort()
    sortedList = unsortedList
    _debug("sortedList: " + ",". join(map(str, sortedList)))

    # Create a global counter for counting the recursive iterations
    _createGlobalCounter()

    return binarySearch(numberToFind, sortedList)

def binarySearch(numToFind, sortedList):
    """Recursively pass in half of the List for searching"""
    _debug("********** binarySearch() **************")

    # Get the global counter for counting the iterations
    global _counter
    _debug("counter: " + str(_counter))

    # Increment global counter
    _counter = _counter + 1
    _debug("numToFind: " + str(numberToFind))

    # First get the length of the List, because it will be reused for checks and helping to break up the List at the middle
    listLen = len(sortedList)
    _debug("Listlen: %d" % listLen)

    # Got empty List, element was not found
    if(listLen == 0):
        _debug("listLen: 0, returning False")
        return False

    # There is only one element in the list so we just need to check if it is a match or not
    elif  listLen == 1:
        _debug("listLen: 1")
        if sortedList[0] == numToFind:
            _debug("Number found. Returning True. sortedLis[0]: %d NumberToFind: %d" % (sortedList[0], numberToFind))
            return True
        else:
            _debug("Number not found. Returning False. sortedLis[0]: %d NumberToFind: %d" % (sortedList[0], numberToFind))
            return False

    # List has at least 2 elements
    else:

        # Find the middle index of the list
        middleIndex = int(listLen // 2)
        _debug("middleIndex: " + str(middleIndex))

        # The value of the middle index element will be reused, so store it
        middleElementValue = sortedList[middleIndex]
        _debug("middleElementValue: " + str(middleElementValue))

        # Check if shooting in the dark was a success
        if middleElementValue == numToFind:

            _debug("The number was ritght in the middle of the list. sortedLis[middleIndex]: %d NumberToFind: %d" \
                   % (sortedList[middleIndex], numberToFind))
            return True


        # Find out which half of the list we want to process further
        else:

            # Use first half of the List containing lower numbers than the value at middle index
            if numberToFind < middleElementValue:
                newList = list(sortedList[: middleIndex])
                _debug("newList: " + ",".join(map(str, newList)))
                return binarySearch(numberToFind, newList)

            # Use first half of the List containing lower numbers than the value at middle index
            elif numberToFind > middleElementValue:
                newList = list(sortedList[middleIndex + 1:])
                _debug("newList: " + ",".join(map(str, newList)))
                return binarySearch(numberToFind, newList)

            # I suck if it ever gets here ...
            else:
                sys.exit("Some serious error happened. Please contact the programmer.")


if __name__ == "__main__":

    # Create a random List containing integers
    unsortedList = getRandomIntList()
    _debug("Unsorted list: " + ",".join(map(str, unsortedList)))

    # Get a random number to search for
    numberToFind = random.randint(1,_LARGEST_NUMBER_IN_LIST)

    # Do the binary search
    search = doBinarySearch(numberToFind, unsortedList)
    _debug("counter: " + str(_counter))

    # Print the result of the search
    print("It took " + str(_counter) + " recursive iterations to find out that: number %d is %sfound in the list: "  % \
          (numberToFind, "not " if not search else "") \
          + ",'".join(map(str, unsortedList)) )