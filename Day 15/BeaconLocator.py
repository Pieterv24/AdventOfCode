import sys
from os import path

def getManhatanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def isWithinSensorRange(testPoint, sensor):
    distance = getManhatanDistance(testPoint, sensor)
    if distance <= sensor[2]:
        return True
    return False
    

def processLines(filePath):
    sensors = set()
    beacons = set()
    for line in open(filePath).readlines():
        splits = line.replace("\n", "").replace("x=", "").replace("y=", "").replace(",", "").replace(":", "").split(" ")
        sX, sY, bX, bY = int(splits[2]),int(splits[3]),int(splits[8]),int(splits[9])
        distance = getManhatanDistance((sX, sY), (bX, bY))

        sensors.add((sX, sY, distance))
        beacons.add((bX, bY))

    allCoords = sensors.union(beacons)
    xMin = min([coord[0] for coord in allCoords])
    xMax = max([coord[0] for coord in allCoords])
    maxDistance = max([sensor[2] for sensor in sensors])
    yCheck = 2000000

    count = 0
    for x in range(xMin-maxDistance, xMax+maxDistance):
        checkCoord = (x, yCheck)
        # print(f"Checking {checkCoord}")
        for sensor in sensors:
            if isWithinSensorRange(checkCoord, sensor) and checkCoord not in beacons:
                count += 1
                break
            else:
                continue

    print(f"Beacon cannot be in {count} places")





if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processLines(filePath)