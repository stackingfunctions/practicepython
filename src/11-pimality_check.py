DEBUG = False

def debug(msg):
    if DEBUG:
        print(msg)

def divisors(num):
    for i in range(2,num):
        if i <= (num / 2):
            debug("num=%d" % num)
            debug("i=%d" % i)
            debug("var=%d" % (num % (i + 1)))
            if num % i == 0:
                debug("Num: %d - returning True" % num)
                return True

    debug("Num: %d - returning False" % num)
    return False


if __name__ == "__main__":

    while True:
        userInput = input("\nWhat number do you want to check for primeness? ")
        if userInput == 'q':
            break
        elif userInput.isdigit():
            userInput = int(userInput)
            if userInput > 3390116:
                print("Sorry too large number. It would take too much time to check this way.")
                continue
            elif userInput == '1':
                print("1 is not a prime")
            else:
                print("%d is %s prime." % (userInput, "not" if divisors(userInput) else "a"))
        else:
            print("Illegal number\n")
            continue

