import sys
from os import path
import functools

valves = dict()

def readValves(filePath):
    for line in open(filePath).readlines():
        valveInfo, pathInfo = line.replace("\n", "").split(";")

        valveInfo = valveInfo.split(" ")
        valveName = valveInfo[1]
        valveFlowRate = int(valveInfo[4].split("=")[1])

        valveAvailablePaths = pathInfo.replace("valves", "valve").split("valve ")[1].split(", ")
        
        valves[valveName] = (valveFlowRate, valveAvailablePaths)

@functools.lru_cache(maxsize=None)
def getHighestPressureRelease(currentValve, minutesLeft, openedValves):
    if minutesLeft <= 0:
        return 0

    best = 0
    if currentValve not in openedValves:
        flow, adjecents = valves[currentValve]
        releasedValue = (minutesLeft - 1) * flow
        current_opened = tuple(sorted(openedValves + (currentValve,)))

        for adjecent in adjecents:
            if releasedValue != 0:
                best = max(best, releasedValue + getHighestPressureRelease(adjecent, minutesLeft - 2, current_opened))
            best = max(best, getHighestPressureRelease(adjecent, minutesLeft - 1, openedValves))
    
    return best
    
    


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        readValves(filePath)
        result = getHighestPressureRelease("AA", 30, ())
        print(result)