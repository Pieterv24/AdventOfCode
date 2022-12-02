import sys
from os import path

class Elf:
    def __init__(self, index, calories):
        self.index = index
        self.calories = calories

def getCalories(elf: Elf):
    return elf.calories

def processCalories(filePath: str):
    file = open(filePath, "r")
    calories = []
    currentCount = 0
    elfIndex = 1
    for line in file.readlines():
        if (line == "\n"):
            calories.append(Elf(elfIndex, currentCount))
            currentCount = 0
            elfIndex += 1
            continue
        currentCount += int(line)
    calories.append(Elf(elfIndex+1, currentCount))
    
    calories.sort(key=getCalories ,reverse=True)
    totalCalories = 0
    for i in range(3):
        winningElf = calories[i]
        totalCalories += winningElf.calories
        print(f"Place {i+1}: Elf {winningElf.index} with {winningElf.calories} calories")
    print(f"Total calories: {totalCalories}")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processCalories(filePath)
