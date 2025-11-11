import sys
from os import path

def processFile(filePath):
    jetPattern = list(open(filePath).readline().replace("\n", ""))
    print(jetPattern)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)