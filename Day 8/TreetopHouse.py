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

def isVisible(grid, x, y):
    row = getRow(grid, y)
    column = getColumn(grid, x)
    treeHeight = int(row[x])
    print(f"checking {x},{y}")
    # row
    frontRow = row[0:x]
    backRow = row[x+1:]
    # column
    frontColumn = column[0:y]
    backColumn = column[y+1:]
    
    frontRow.sort(reverse=True)
    backRow.sort(reverse=True)
    frontColumn.sort(reverse=True)
    backColumn.sort(reverse=True)

    return frontRow[0] < treeHeight or backRow[0] < treeHeight or frontColumn[0] < treeHeight or backColumn[0] < treeHeight

def findVisibleTrees(grid):
    visibleCouter = len(grid) * 2 + (len(grid[0]) - 2) * 2
    print(f"{visibleCouter} trees on the edges")

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            visibleCouter += 1 if isVisible(grid, x, y) else 0
    
    print(f"{visibleCouter} trees are visible")

def createGrid(filePath: str):
    grid = []
    for row in open(filePath).readlines():
        rowArr = []
        for i in list(row.replace("\n", "")):
            rowArr.append(int(i))
        grid.append(rowArr)
    printGrid(grid)

    findVisibleTrees(grid)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        createGrid(filePath)