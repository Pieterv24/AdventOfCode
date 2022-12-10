import sys
from os import path

cycles = 240

def parseAddX(command):
    commandText, value = command.replace("\n", "").split(" ")
    value = int(value)
    return (commandText, value)

def processInstructions(filePath):
    instructions = open(filePath).readlines()
    displayRow = []
    display = []

    commandIndex = 0
    addCommandProgress = 0
    spritePos = 1
    for cycle in range(cycles):
        pixelPos = cycle - (len(display) * 40)
        if (pixelPos >= spritePos-1 and pixelPos <= spritePos+1):
            displayRow.append("#")
            if (len(displayRow) == 40):
                display.append(displayRow)
                displayRow = []
        else:
            displayRow.append(".")
            if (len(displayRow) == 40):
                display.append(displayRow)
                displayRow = []

        instruction = instructions[commandIndex]
        if addCommandProgress > 0:
            _, addValue = parseAddX(instruction)
            spritePos += addValue
            addCommandProgress = 0
            commandIndex += 1
            continue
        elif "noop" in instruction:
            commandIndex += 1
        elif "addx" in instruction:
            addCommandProgress = 1

    displayOutput = ""
    joinChar = ""
    for row in display:
        displayOutput += f"{joinChar.join(row)}\n"

    print(displayOutput)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processInstructions(filePath)