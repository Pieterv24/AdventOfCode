import sys
from os import path

peekCycles = [20, 60, 100, 140, 180, 220]

def parseAddX(command):
    commandText, value = command.replace("\n", "").split(" ")
    value = int(value)
    return (commandText, value)

def shouldCheckRegister(cycle, commandCycles, registerValue):
    for peekMoment in peekCycles:
        if (cycle <= peekMoment and cycle >= peekMoment - commandCycles):
            print(f"Cycle: {cycle} peeking for: {peekMoment} with value: {registerValue}")
            peekCycles.remove(peekMoment)
            return peekMoment*registerValue
    return 0

def processInstructions(filePath):
    instructions = open(filePath).readlines()
    peeks = []

    registerValue = 1
    currentCycle = 0
    result = 0
    for instruction in instructions:
        print(instruction)
        if "noop" in instruction:
            result += shouldCheckRegister(currentCycle, 1, registerValue)
            currentCycle += 1
            print(f"cycle: {currentCycle} Register: {registerValue}")
        elif "addx" in instruction:
            result += shouldCheckRegister(currentCycle, 2, registerValue)
            currentCycle += 2
            _, value = parseAddX(instruction)
            registerValue += value
            print(f"cycle: {currentCycle} Register: {registerValue}")
    
    print(result)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processInstructions(filePath)