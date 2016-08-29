
def removeDuplicatesLoop(l):
    retList = []
    for element in l:
        if element not in retList:
            retList.append(element)
    return retList

def removeDuplicatesSet(l):
    return set(l)

if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 3, 5, 6, 7, 7, 8, 6, 9]
    refList = [1,2,3,4,5,6,7,8,9]

    loopResult = removeDuplicatesLoop(l)
    print("loopResult: ", loopResult)
    setResult = list(removeDuplicatesSet(l))
    print("setResult: ", setResult)

    if(len(set(loopResult).intersection(refList)) == len(refList)):
        print("loopResult is correct")

    if (len(set(setResult).intersection(refList)) == len(refList)):
        print("loopResult is correct")