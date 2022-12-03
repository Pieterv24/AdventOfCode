import sys
from os import path
import numpy as np

def calculatePriority(inputChar: str):
    if (len(inputChar) > 1):
        print("Invalid input")
        return 0
    asciiValue = ord(inputChar)
    # value is lowercase
    if (asciiValue >= 97):
        return asciiValue - 96
    else:
        return asciiValue - 38

def findOddRucksackItem(rugsackContents: str):
    arr = list(rugsackContents.replace("\n", ""))
    Comp1, Comp2 = np.array_split(arr, 2)
    return np.intersect1d(Comp1, Comp2)[0]

def checkRucksacks(filePath: str):
    priority = 0
    for rucksack in open(filePath).readlines():
        priority += calculatePriority(findOddRucksackItem(rucksack))
    
    print(f"Total priority: {priority}")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        checkRucksacks(filePath)