import sys
from os import path

# A: Rock
# B: Paper
# C: Scissors
# X: Rock?
# Y: Paper?
# Z: Scissors

def calculatePlayerResult(oponent: str, player: str):
    match player:
        case "X": # ROCK
            if (oponent == "A"): return 4    # ROCK:     DRAW
            elif (oponent == "B"): return 1  # PAPER:    LOSE
            elif (oponent == "C"): return 7  # SCISSORS: WIN
        case "Y": # PAPER
            if (oponent == "A"): return 8    # ROCK:     WIN
            elif (oponent == "B"): return 5  # PAPER:    DRAW
            elif (oponent == "C"): return 2  # SCISSORS: LOSE
        case "Z": # Scissors
            if (oponent == "A"): return 3    # ROCK:     LOSE
            elif (oponent == "B"): return 9  # PAPER:    WIN
            elif (oponent == "C"): return 6  # SCISSORS: DRAW
        case _:
            return 0

def processStrategy(filePath: str):
    score = 0;
    for round in open(filePath).readlines():
        roundEntries = round.replace("\n", "").split(" ");
        score += calculatePlayerResult(roundEntries[0], roundEntries[1])

    print(f"Score is {score}")



if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processStrategy(filePath)