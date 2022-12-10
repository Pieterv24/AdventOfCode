import sys
from os import path
import math

class Grid():
    def __init__(self):
        self.size = 1000
        self.startOffset = int(self.size/2)
        self.grid = []
        for row in range(self.size):
            rowData = []
            for col in range(self.size):
                rowData.append(False)
            self.grid.append(rowData)

    def registerTailVisit(self, tailPos):
        self.grid[tailPos[1]+self.startOffset][tailPos[0]+self.startOffset] = True

    def countVisits(self):
        count = 0
        for row in self.grid:
            for col in row:
                count += 1 if col else 0
        
        return count

    def printGrid(self, positions):
        rows = []
        head = positions[0]
        for y, row in enumerate(self.grid):
            rowBuilder = ""
            for x, col in enumerate(row):
                if (head[0]+self.startOffset == x and head[1]+self.startOffset == y):
                    rowBuilder += "H"
                    continue
                knotFound = False
                for i in range(len(positions)-1):
                    knot = positions[i+1]
                    if (knot[0]+self.startOffset == x and knot[1]+self.startOffset == y):
                        rowBuilder += f"{i+1}"
                        knotFound = True
                        break
                if (self.startOffset == x and self.startOffset == y and not knotFound):
                    rowBuilder += "s"
                    continue
                elif (not knotFound):
                    rowBuilder += "*" if col else "."
            rows.append(rowBuilder)
        rows.reverse()
        return "\n".join(rows)

    def __str__(self) -> str:
        strBuilder = ""
        for row in self.grid:
            strBuilder += f"{row}\n"
        return strBuilder

def readInstructions(fileLines):
    instructions = []
    for line in fileLines:
        direction, count = line.split(" ")
        count = int(count)
        instructions.append((direction, count))
    return instructions

def moveHead(direction, currentPosition):
    match direction:
        case 'U':
            return [currentPosition[0], currentPosition[1]+1]
        case 'D':
            return [currentPosition[0], currentPosition[1]-1]
        case 'L':
            return [currentPosition[0]-1, currentPosition[1]]
        case 'R':
            return [currentPosition[0]+1, currentPosition[1]]
        
def updateTail(direction, currentPos, headPos):
    tailShouldUpdate = not ((math.fabs(currentPos[0] - headPos[0]) <= 1) and (math.fabs(currentPos[1] - headPos[1]) <= 1))
    if tailShouldUpdate:
        xDelta = currentPos[0] - headPos[0]
        yDelta = currentPos[1] - headPos[1]
        # RIGHT
        if xDelta < -1:
            if yDelta < 0:
                return [currentPos[0]+1, currentPos[1]+1]
            if yDelta > 0:
                return [currentPos[0]+1, currentPos[1]-1]
            return [currentPos[0]+1, currentPos[1]]
        # LEFT
        if xDelta > 1:
            if yDelta < 0:
                return [currentPos[0]-1, currentPos[1]+1]
            if yDelta > 0:
                return [currentPos[0]-1, currentPos[1]-1]
            return [currentPos[0]-1, currentPos[1]]
        # DOWN
        if yDelta > 1:
            if xDelta < 0:
                return [currentPos[0]+1, currentPos[1]-1]
            if xDelta > 0:
                return [currentPos[0]-1, currentPos[1]-1]
            return [currentPos[0], currentPos[1]-1]
        # UP
        if yDelta < -1:
            if xDelta < 0:
                return [currentPos[0]+1, currentPos[1]+1]
            if xDelta > 0:
                return [currentPos[0]-1, currentPos[1]+1]
            return [currentPos[0], currentPos[1]+1]
    else:
        return currentPos


def processFile(filePath):
    instructions = readInstructions(open(filePath).readlines())
    ropes = 10
    ropePositions = []
    for i in range(ropes):
        ropePositions.append([0, 0])
    grid = Grid()

    for instruction in instructions:
        for times in range(instruction[1]):
            ropePositions[0] = moveHead(instruction[0], ropePositions[0])
            for i in range(ropes-1):
                ropePositions[i+1] = updateTail(instruction[0], ropePositions[i+1], ropePositions[i])
            grid.registerTailVisit(ropePositions[ropes-1])
            # print(f"{grid.printGrid(ropePositions)}\n")
        # print(f"{instruction[0]}\n{grid.printGrid(ropePositions)}\n")

    print(f"{grid.printGrid(ropePositions)}\n")
    print(f"Tail visited: {grid.countVisits()}")





if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)