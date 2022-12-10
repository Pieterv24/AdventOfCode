import sys
from os import path
import math

class Grid():
    def __init__(self):
        self.size = 1000
        self.startOffset = int(self.size/2)
        # self.grid = [[False]];
        self.grid = []
        for row in range(self.size):
            rowData = []
            for col in range(self.size):
                rowData.append(False)
            self.grid.append(rowData)

    # def growGrid(self, newSize):
    #     yGrow = newSize - self.size
    #     for y in range(yGrow):
    #         newArray = []
    #         for x in range(newSize):
    #             newArray.append(False)
    #         self.grid.append(newArray)

    #     for index, row in enumerate(self.grid):
    #         xGrow = newSize - len(row)
    #         if xGrow >= 1:
    #             for i in range(xGrow):
    #                 self.grid[index].append(False)
    #     self.size = newSize

    def registerTailVisit(self, tailPos):
        # if (tailPos[0]+1 > self.size or tailPos[1]+1 > self.size):
        #     self.growGrid(tailPos[0]+1 if tailPos[0]+1 > tailPos[1]+1 else tailPos[1]+1)
        self.grid[tailPos[1]+self.startOffset][tailPos[0]+self.startOffset] = True

    def countVisits(self):
        count = 0
        for row in self.grid:
            for col in row:
                count += 1 if col else 0
        
        return count

    def printGrid(self, head, tail):
        rows = []
        for y, row in enumerate(self.grid):
            rowBuilder = ""
            for x, col in enumerate(row):
                if (head[0]+self.startOffset == x and head[1]+self.startOffset == y):
                    rowBuilder += "H"
                elif (tail[0]+self.startOffset == x and tail[1]+self.startOffset == y):
                    rowBuilder += "T"
                else:
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
        match direction:
            case 'U':
                if math.fabs(xDelta) > 0:
                    return [headPos[0], currentPos[1]+1]
                return [currentPos[0], currentPos[1]+1]
            case 'D':
                if math.fabs(xDelta) > 0:
                    return [headPos[0], currentPos[1]-1]
                return [currentPos[0], currentPos[1]-1]
            case 'L':
                if math.fabs(yDelta) > 0:
                    return [currentPos[0]-1, headPos[1]]
                return [currentPos[0]-1, currentPos[1]]
            case 'R':
                if math.fabs(yDelta) > 0:
                    return [currentPos[0]+1, headPos[1]]
                return [currentPos[0]+1, currentPos[1]]
    else:
        return currentPos


def processFile(filePath):
    instructions = readInstructions(open(filePath).readlines())
    headPos = [0, 0]
    tailPos = [0, 0]
    grid = Grid()

    for instruction in instructions:
        # print(f"{instruction[0]}: {instruction[1]}")
        for times in range(instruction[1]):
            headPos = moveHead(instruction[0], headPos)
            # if headPos[0]+1 > len(grid.grid):
            #     grid.growGrid(headPos[0]+1)
            # elif headPos[1]+1 > len(grid.grid):
            #     grid.growGrid(headPos[1]+1)
            tailPos = updateTail(instruction[0], tailPos, headPos)
            grid.registerTailVisit(tailPos)

    print(f"{grid.printGrid(headPos, tailPos)}\n")
    print(f"Tail visited: {grid.countVisits()}")





if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)