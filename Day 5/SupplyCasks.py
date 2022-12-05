import sys
from os import path

def doMove(stacks, source, target, amount):
    for i in range(amount):
        stacks[target-1].append(stacks[source-1].pop())

def createStacks(lines):
    lines.reverse()
    stacks = []
    stackCount = 0
    for line in lines:
        if "[" not in line:
            stackCount = int(line.split(" ")[len(line.split(" ")) - 2])
            for i in range(stackCount):
                stacks.append([])
            print(f"{stackCount} stacks found")
            continue
        for i in range(stackCount):
            item = line[1+(i*4)]
            if item != " ":
                stacks[i].append(item)
    return stacks

def parseMoveInstruction(instruction):
    split = instruction.replace("\n", "").split(" ")
    return int(split[1]), int(split[3]), int(split[5])


def processLines(filePath):
    stacksCreated = False
    stackBuffer = []
    stacks = []
    for line in open(filePath).readlines():
        if (line == "\n"):
            stacks = createStacks(stackBuffer)
            stacksCreated = True
            print(stacks)
            continue
        if (stacksCreated):
            count, source, target = parseMoveInstruction(line)
            print(f"{count} from {source} to {target}")
            doMove(stacks, source, target, count)
        else:
            stackBuffer.append(line.replace("\n", ""))
    result = ""
    for stack in stacks:
        result += stack[len(stack)-1]
    print(result)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processLines(filePath)