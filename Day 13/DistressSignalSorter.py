import sys
from os import path
from functools import cmp_to_key

def comparePackets(pair):
    left, right = pair
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            result = comparePackets((left[index], right[index]))
            if result == 1:
                return 1
            elif result == -1:
                return -1
            else:
                index += 1
        if index == len(left) and index < len(right):
            return -1
        elif index == len(right) and index < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return comparePackets(([left], right))
    elif isinstance(left, list) and isinstance(right, int):
        return comparePackets((left, [right]))
            
            

def processFile(filePath):
    packets = []
    for line in open(filePath).readlines():
        if line != "\n":
            array = eval(line)
            packets.append(array)
    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=cmp_to_key(lambda left, right: comparePackets((left, right))))
    
    result = 1
    for index, packet in enumerate(packets):
        if packet == [[6]] or packet == [[2]]:
            result *= (index + 1)

    print(result)
            



if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)