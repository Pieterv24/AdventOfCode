import sys
from os import path

def getManhatanDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def isValidBeaconLocation(checkCoord, sensors):
    for sensor in sensors:
        if getManhatanDistance(checkCoord, sensor) <= sensor[2]:
            return False
    return True
    

def processLines(filePath):
    sensors = set()
    beacons = set()
    for line in open(filePath).readlines():
        splits = line.replace("\n", "").replace("x=", "").replace("y=", "").replace(",", "").replace(":", "").split(" ")
        sX, sY, bX, bY = int(splits[2]),int(splits[3]),int(splits[8]),int(splits[9])
        distance = getManhatanDistance((sX, sY), (bX, bY))

        sensors.add((sX, sY, distance))
        beacons.add((bX, bY))

    maxRange = 4000000
    foundBeacon = False

    # If there is only one possible location.
    # The beacon should be at a location that is the distance of a sensor + 1
    for sensor in sensors:
        sX, sY, distance = sensor
        # Check all positions at von neumann neigbor range of distance + 1
        for quadrantX in range(distance+2):
            if (foundBeacon):
                break
            quadrantY = (distance+1)-quadrantX
            
            # Check for all 4 quadrants
            for xMod, yMod in [(1,1), (-1,1), (-1,-1), (1,-1)]:
                checkCoord = (sX+(quadrantX*xMod), sY+(quadrantY*yMod))
                if not (0<=checkCoord[0]<=maxRange and 0<=checkCoord[1]<=maxRange):
                    continue
                if isValidBeaconLocation(checkCoord, sensors):
                    print(f"Found coord at {checkCoord} answer is {checkCoord[0]*4000000+checkCoord[1]}")
                    foundBeacon = True
                    break

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processLines(filePath)