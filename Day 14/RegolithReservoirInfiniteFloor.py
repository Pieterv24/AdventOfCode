import sys
from os import path

def getRockFormations(filePath):
    rocks = set()

    for line in open(filePath).readlines():
        points = line.replace("\n", "").split(" -> ")
        prev = None
        for point in points:
            x,y = point.split(",")
            x,y = int(x),int(y)
            if prev is not None:
                xDiff = x-prev[0]
                yDiff = y-prev[1]
                veinLength = max(abs(xDiff), abs(yDiff))
                for i in range(veinLength+1):
                    xPos = prev[0] + i*(1 if xDiff > 0 else (-1 if xDiff < 0 else 0))
                    yPos = prev[1] + i*(1 if yDiff > 0 else (-1 if yDiff < 0 else 0))
                    rocks.add((xPos, yPos))
            prev = (x, y)
    return rocks

def drawFormations(floor, formations, sand, start):
    items = formations.union(sand)
    xMin = min([item[0] for item in items])
    xMax = max([item[0] for item in items])
    for y in range(floor+1):
        row = ""
        for x in range(xMax-xMin+1):
            if (x+xMin, y) in formations:
                row += "#"
            elif (x+xMin, y) in sand:
                row += "o"
            elif (x+xMin, y) == start:
                row += "+"
            elif y == floor:
                row += "#"
            else:
                row += "."
        print(row)

def sandCanMove(currentUnit, sand, rocks, floor):
    x, y = currentUnit
    if (x, y+1) in sand or (x,y+1) in rocks:
        if (x-1,y+1) in sand or (x-1,y+1) in rocks:
            if (x+1,y+1) in sand or (x+1,y+1) in rocks:
                return False
    if y + 1 == floor:
        return False
    return True


def processFile(filePath):
    # Get a set of all rock locations
    rockFormations = getRockFormations(filePath)
    sand = set()
    start = (500, 0)
    # Get cave limits (for creating grid)
    floor = max([rock[1] for rock in rockFormations]) + 2

    drawFormations(floor, rockFormations, sand, start)

    sandBlocked = False
    while not sandBlocked:
        currentUnit = start
        while(sandCanMove(currentUnit, sand, rockFormations, floor)):
            x, y = currentUnit
            if not ((x, y+1) in sand or (x,y+1) in rockFormations):
                currentUnit = (x, y+1)
            elif not ((x-1, y+1) in sand or (x-1,y+1) in rockFormations):
                currentUnit = (x-1, y+1)
            else:
                currentUnit = (x+1, y+1)
        if currentUnit != start:
            sand.add(currentUnit)
        else:
            sand.add(currentUnit)
            sandBlocked = True

    print(f"Sand has stopped in {len(sand)} units")
    drawFormations(floor, rockFormations, sand, start)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)