import sys
from os import path
import math
from collections import deque

# Convert a..z to 1..26
def charToValue(char):
    asciiValue = ord(char)
    return asciiValue - 96

# Create grid and convert letters to values
# Return grid and start/endpoint
def createHeightGrid(filePath):
    startPoint = (0, 0)
    bestPoint = (0, 0)
    grid = []
    for y, line in enumerate(open(filePath).readlines()):
        row = list(line.replace("\n", ""))
        newRow = []
        for x, char in enumerate(row):
            if char == "S":
                startPoint = (y, x)
                newRow.append(charToValue('a'))
            elif char == "E":
                bestPoint = (y, x)
                newRow.append(charToValue('z'))
            else:
                newRow.append(charToValue(char))
        grid.append(newRow)
    
    return (startPoint, bestPoint, grid)

def findPathBFS(start, end, grid):
    queue = deque()
    
    # Add all positions of height 1 to the queue (paths will be started for all of them) the first one will return the amount of steps
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if(grid[row][column] == 1):
                queue.append(((row, column), 0))

    # List of visited positions
    visited = set()
    # Run for as long as there is items in the queue
    while queue:
        # Read first item from queue
        (row, col), distance = queue.popleft()
        # Skip if already visited
        if (row, col) in visited:
            continue
        # Register as visited
        visited.add((row, col))
        # Check if end position is reached
        if (row, col) == end:
            return distance
        # Check next positions
        for rMod, cMod in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = row + rMod
            newC = col + cMod
            
            # Check if new position is inside grid and if we can travel to the next position
            # If we can travel and it's on the grid, add it to the queue
            if (0<=newR<len(grid) and 
                0<=newC<len(grid[0]) and 
                grid[newR][newC]<=1+grid[row][col]):
                queue.append(((newR, newC), distance+1))

def processFile(filePath):
    startPoint, bestPoint, grid = createHeightGrid(filePath)

    path = findPathBFS(startPoint, bestPoint, grid)
    print(path)
    
    
    

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)