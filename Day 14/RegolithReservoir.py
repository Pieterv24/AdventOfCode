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

def drawFormations(floor, xMin, xMax, formations, sand, start, endPath = set()):
    for y in range(floor+1):
        row = ""
        for x in range(xMax-xMin+1):
            if (x+xMin, y) in formations:
                row += "#"
            elif (x+xMin, y) in sand:
                row += "o"
            elif (x+xMin, y) == start:
                row += "+"
            elif (x+xMin, y) in endPath:
                row += "~"
            else:
                row += "."
        print(row)

def sandCanMove(currentUnit, sand, rocks):
    x, y = currentUnit
    if (x, y+1) in sand or (x,y+1) in rocks:
        if (x-1,y+1) in sand or (x-1,y+1) in rocks:
            if (x+1,y+1) in sand or (x+1,y+1) in rocks:
                return False
    return True


def processFile(filePath):
    # Get a set of all rock locations
    rockFormations = getRockFormations(filePath)
    sand = set()
    start = (500, 0)
    # Get cave limits (for creating grid)
    floor = max([rock[1] for rock in rockFormations])
    xMin = min([rock[0] for rock in rockFormations])
    xMax = max([rock[0] for rock in rockFormations])

    drawFormations(floor, xMin, xMax, rockFormations, sand, start)

    sandInAbbys = False
    path = set()
    while not sandInAbbys:
        currentUnit = start
        while(sandCanMove(currentUnit, sand, rockFormations)):
            x, y = currentUnit
            path.add(currentUnit)
            if (y > floor):
                sandInAbbys = True
                break
            if not ((x, y+1) in sand or (x,y+1) in rockFormations):
                currentUnit = (x, y+1)
            elif not ((x-1, y+1) in sand or (x-1,y+1) in rockFormations):
                currentUnit = (x-1, y+1)
            else:
                currentUnit = (x+1, y+1)
        
        if not sandInAbbys:
            sand.add(currentUnit)
            path = set()
    print(f"Abyss reached in {len(sand)} units")
    drawFormations(floor, xMin, xMax, rockFormations, sand, start, path)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)