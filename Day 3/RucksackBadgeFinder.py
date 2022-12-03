import sys
from os import path
import numpy as np
from typing import MutableSequence

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

def findBadgeRucksackItem(group: MutableSequence):
    elf1 = list(group[0].replace("\n", ""))
    elf2 = list(group[1].replace("\n", ""))
    elf3 = list(group[2].replace("\n", ""))

    intersect1 = np.intersect1d(elf1, elf2)
    return np.intersect1d(intersect1, elf3)[0]

def checkRucksacks(filePath: str):
    priority = 0
    lines = open(filePath).readlines()
    groups =  np.array_split(lines, len(lines)/3)
    for group in groups:
        priority += calculatePriority(findBadgeRucksackItem(group))
    
    print(f"Total priority: {priority}")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        checkRucksacks(filePath)