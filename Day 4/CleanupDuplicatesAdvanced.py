import sys
from os import path



def findCompleteOverlaps(filePath):
    fullyEnvelopedCount = 0
    for pair in open(filePath).readlines():
        entry = pair.replace("\n", "").replace(",", "-").split("-")
        print(entry)
        if ((int(entry[0]) >= int(entry[2]) and int(entry[1]) <= int(entry[3])) or 
            (int(entry[2]) >= int(entry[0]) and int(entry[3]) <= int(entry[1])) or
            (int(entry[1]) >= int(entry[2]) and int(entry[1]) <= int(entry[3])) or
            (int(entry[3]) >= int(entry[0]) and int(entry[3]) <= int(entry[1]))):
            print("Found covering range")
            fullyEnvelopedCount += 1
    print(f"{fullyEnvelopedCount} ranges are fully covered by the other")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        findCompleteOverlaps(filePath)