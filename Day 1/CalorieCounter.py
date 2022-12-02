import sys
from os import path

def processCalories(filePath: str):
    file = open(filePath, "r")
    elfIndex = 1
    highestCount = 0
    hightestIndex = 0
    currentCount = 0
    for line in file.readlines():
        if (line == "\n"):
            if (currentCount > highestCount):
                hightestIndex = elfIndex
                highestCount = currentCount
            elfIndex += 1
            currentCount = 0
            continue
        currentCount += int(line)
    
    print(f"Elf: {hightestIndex} is carrying {highestCount} calories")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processCalories(filePath)
