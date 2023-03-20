import sys
from os import path
import time

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
      
        filePath = sys.argv[1]
        print(f"Processing {filePath}...\n")
        time.sleep(2)
        file = open(filePath, 'r')
        file_content = file.read()
        print(file_content)
        f.close()
