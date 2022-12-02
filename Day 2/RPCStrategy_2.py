import sys
from os import path

# A: Rock
# B: Paper
# C: Scissors
# X: Rock?
# Y: Paper?
# Z: Scissors

def calculateResponseResult(oponent: str, result: str):
    match result:
        case "X": # LOSE
            if (oponent == "A"): return 3    # ROCK:    SCISSORS
            elif (oponent == "B"): return 1  # PAPER:   ROCK
            elif (oponent == "C"): return 2  # SCISSORS:PAPER
        case "Y": # DRAW
            if (oponent == "A"): return 4    # ROCK:    ROCK
            elif (oponent == "B"): return 5  # PAPER:   PAPER
            elif (oponent == "C"): return 6  # SCISSORS:SCISSORS
        case "Z": # WIN
            if (oponent == "A"): return 8    # ROCK:    PAPER
            elif (oponent == "B"): return 9  # PAPER:   SCISSORS
            elif (oponent == "C"): return 7  # SCISSORS:ROCK
        case _:
            return 0

def processStrategy(filePath: str):
    score = 0;
    for round in open(filePath).readlines():
        roundEntries = round.replace("\n", "").split(" ");
        score += calculateResponseResult(roundEntries[0], roundEntries[1])

    print(f"Score is {score}")



if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processStrategy(filePath)