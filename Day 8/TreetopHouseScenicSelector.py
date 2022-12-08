import sys
from os import path

def printGrid(grid):
    for row in grid:
        print(row)

def getRow(grid, row: int):
    return grid[row]

def getColumn(grid, column: int):
    columnArr = []
    for row in grid:
        columnArr.append(row[column])
    return columnArr

def getViewDistance(row, height):
    counter = 0
    for item in row:
        if item >= height:
            counter += 1
            break
        counter += 1
    return counter

def calculateScenicScore(grid, x, y):
    row = getRow(grid, y)
    column = getColumn(grid, x)
    treeHeight = int(row[x])
    score = 0

    # row
    frontRow = row[0:x]
    backRow = row[x+1:]
    # column
    frontColumn = column[0:y]
    backColumn = column[y+1:]
    
    frontRow.reverse()
    frontColumn.reverse()

    return getViewDistance(frontRow, treeHeight) * getViewDistance(backRow, treeHeight) * getViewDistance(frontColumn, treeHeight) * getViewDistance(backColumn, treeHeight)


def iterateTrees(grid):
    bestScore = 0

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            print(f"Checking {x}, {y}")
            score = calculateScenicScore(grid, x, y)
            if score > bestScore:
                bestScore = score
    
    print(f"Best score is: {bestScore}")
    

def createGrid(filePath: str):
    grid = []
    for row in open(filePath).readlines():
        rowArr = []
        for i in list(row.replace("\n", "")):
            rowArr.append(int(i))
        grid.append(rowArr)
    printGrid(grid)

    iterateTrees(grid)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        createGrid(filePath)