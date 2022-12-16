import sys
from os import path
import functools

tunnels = dict()
rates = dict()

def readValves(filePath):
    for line in open(filePath).readlines():
        valveInfo, pathInfo = line.replace("\n", "").split(";")

        valveInfo = valveInfo.split(" ")
        valveName = valveInfo[1]
        valveFlowRate = int(valveInfo[4].split("=")[1])

        valveAvailablePaths = pathInfo.replace("valves", "valve").split("valve ")[1].split(", ")
        
        tunnels[valveName] = valveAvailablePaths
        # We don't need any values that don't have any flowrate
        if valveFlowRate > 0:
            rates[valveName] = valveFlowRate

#Cache this function to speed up operation
@functools.cache
def getDistance(cur, target, visited=set()):
    if cur == target:
        return 0
    if target in visited:
        return float("inf")
    visited.add(target)
    shortest = min(getDistance(cur, path) for path in tunnels[target])
    visited.remove(target)
    return shortest + 1

def total(current, time, valves):
    result = 0
    for valve in valves:
        new_time = time - getDistance(current, valve) - 1
        if new_time <= 0:
            continue
        new_nodes = tuple(n for n in valves if n != valve)
        result = max(result, new_time * rates[valve] + total(valve, new_time, new_nodes))
    return result

def findMaxPressureRelease():
    result = 0
    # Create partitions to loop through every combination of opened valves by both me & elepahant
    for partition in range(1 << (len(rates) - 1)):
        print(f"Partition: {partition}, current result: {result}")
        me = tuple(valve for i, valve in enumerate(rates) if partition & (1 << i))
        elephant = tuple(valve for i, valve in enumerate(rates) if not partition & (1 << i))
        result = max(result, total("AA", 26, me) + total("AA", 26, elephant))
    return result


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        readValves(filePath)
        result = findMaxPressureRelease()
        print(result)