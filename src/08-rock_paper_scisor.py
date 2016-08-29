import sys
import random
import time

availablePicks = ("rock", "paper", "scisors")
random.seed = time.localtime()

while True:
    winner = None
    machinePick = None

    print()
    playerPick = input("Pick one (rock, paper, scisors), or 'q' for quitting the game: ").lower()

    if playerPick == "q":
        sys.exit()
    if playerPick not in availablePicks:
        print("Illegal value")
        continue
    else:
        machinePick = availablePicks[random.randint(0,2)]

        if playerPick == machinePick:
            print("Tie! We both picked: %s" % playerPick)
            continue
        elif playerPick == "rock":
            winner = "Me" if machinePick == "paper" else "You"
        elif playerPick == "paper":
            winner = "Me" if machinePick == "scisors" else "You"
        elif playerPick == "scisors":
            winner = "Me" if machinePick == "rock" else "You"

    print("You picked: %s, I picked: %s. The winner is: %s" % (playerPick, machinePick, winner))

