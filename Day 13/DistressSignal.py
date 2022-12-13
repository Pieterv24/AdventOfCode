import sys
from os import path

def processPair(pair):
    left, right = pair
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            result = processPair((left[index], right[index]))
            if result == True:
                return True
            elif result == False:
                return False
            else:
                index += 1
        if index == len(left) and index < len(right):
            return True
        elif index == len(right) and index < len(left):
            return False
        else:
            return None
    elif isinstance(left, int) and isinstance(right, list):
        return processPair(([left], right))
    elif isinstance(left, list) and isinstance(right, int):
        return processPair((left, [right]))
            
            

def processFile(filePath):
    pairs = []
    pairBuffer = []
    for line in open(filePath).readlines():
        if line == "\n":
            pairs.append((pairBuffer[0], pairBuffer[1]))
            pairBuffer = []
            continue
        array = eval(line)
        pairBuffer.append(array)
    if len(pairBuffer) > 0:
        pairs.append((pairBuffer[0], pairBuffer[1]))
        pairBuffer = []

    answer = 0
    for index, pair in enumerate(pairs):
        print(pair)
        if processPair(pair):
            print(f"{index+1} is correct")
            answer += (index+1)

    print(f"{answer}")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)