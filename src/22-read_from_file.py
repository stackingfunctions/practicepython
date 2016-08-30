_DEBUG = False
_FILE_1 = "../tmp/22-nameslist.txt"
_FILE_2 = "../tmp/22-Training_01.txt"

def _debug(msg):
    if _DEBUG: print("[DEBUG] " + msg)

def getDataFromLine(line):
    """Helper function for processSolution() so it can be called for both solutions.
    This function will return the data we are interested in."""
    _debug("line: " + line)

    # The line contains '/' so we need to split the string
    if line.find("/") != -1:

        # In certain cases there are subcategories like indoor/outdoor,
        # but if I take that into consideration, the result will be so boring (the same 50 for all)
        return line.split("/")[2]

    # Value is coming from the first file and it contains only the data without any extra
    else:
        return line

def processSolution(myhash, open_file):
    """The main processing of both solutions."""

    # We will break when needed
    while True:

        # Make sure we strip '\n' from the end of the line
        data = getDataFromLine(open_file.readline().strip())

        # EOF returns '' - break at the end of file
        if data == '':
            break

        # If key was already initialized, increment it's value
        try:
            myhash[data] += 1

        # This is teh first time we encounter this key
        except KeyError:
            myhash[data] = 1


def simpleSoultion():
    """Counts distinct elements in the first file."""
    myhash = {}
    with open(_FILE_1, "r") as open_file:
        processSolution(myhash, open_file)
    return myhash


def challengeSolution():
    """Counts distinct elements in the second file."""
    myhash = {}
    with open(_FILE_2, "r") as open_file:
        processSolution(myhash, open_file)
    return myhash

def printHash(myhash, filename):
    """Prints the myhash containing the results."""
    for k,v in myhash.items():
        print("File (%s) contains '%s': %d times." % (filename, k, v))

if __name__ == "__main__":

    # Simple solution
    print("Solution to the easy part #1:\n")
    printHash(simpleSoultion(), _FILE_1)

    # Solution to the not real challenge ;-)
    print("\n\nSolution to the not so hard #2\n")
    printHash(challengeSolution(), _FILE_2)