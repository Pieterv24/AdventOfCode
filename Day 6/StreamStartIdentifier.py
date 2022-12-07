import sys
from os import path

def checkForDuplicates(buffer):
    if len(buffer) == len(set(buffer)):
        return True
    return False

def processStream(stream):
    buffer = []
    for i, char in enumerate(stream):
        buffer.append(char);
        if len(buffer) >= 4:
            if checkForDuplicates(buffer):
                print(f"Start sequence found comms start on {i+1}")
                break
            del buffer[0]

def readFile(filePath):
    for line in open(filePath).readlines():
        processStream(line)
        

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        readFile(filePath)