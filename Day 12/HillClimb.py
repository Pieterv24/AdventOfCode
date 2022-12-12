import sys
from os import path

def charToValue(char):
    asciiValue = ord(char)
    return asciiValue - 96

def createHeightGrid(filePath):
    startPoint = (0, 0)
    bestPoint = (0, 0)
    grid = []
    for x, line in enumerate(open(filePath).readlines()):
        row = list(line.replace("\n", ""))
        newRow = []
        for y, char in enumerate(row):
            if char == "S":
                startPoint = (x, y)
                newRow.append(charToValue('a'))
            elif char == "E":
                bestPoint = (x, y)
                newRow.append(charToValue('z'))
            else:
                newRow.append(charToValue(char))
        grid.append(newRow)
    
    return (startPoint, bestPoint, grid)

def processFile(filePath):
    startPoint, bestPoint, grid = createHeightGrid(filePath)
    print(startPoint)
    print(bestPoint)
    print(grid)
    

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)