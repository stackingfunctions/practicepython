import random
import time
import string
import sys

random.seed(time.localtime())

WEAK = 0
STRONG = 1

weakPasses = ("yoyo97", 'passwd', "roodolf", "foo", "try again")

strongCharacters = string.punctuation + string.ascii_letters + string.digits

def getUserInput():
    ui = input("For weak password enter '0', for strong enter '1' ")
    if ui == 'q':
        sys.exit()
    if ui.isdigit() and (ui == str(WEAK) or ui == str(STRONG)):
        return int(ui)
    else:
        print("Bad input")

def generatePassword(strength):
    return weakPasses[random.randint(0, len(weakPasses) - 1)] if strength == WEAK else "".join(random.sample(strongCharacters, random.randint(6, 12)))


if __name__ == "__main__":
    while True:
        print("Your generated password is: ", generatePassword(getUserInput()))