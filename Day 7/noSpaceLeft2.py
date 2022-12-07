import sys
from os import path
import math

class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = dict()
    def addFile(self, file, path):
        newPath = path[:]
        if len(path) == 0:
            self.files.append(file)
        else:
            del newPath[0]
            self.dirs[path[0]].addFile(file, newPath)
    def addDir(self, name, path):
        newPath = path[:]
        if len(path) == 0:
            self.dirs[name] = Dir(name)
        else:
            del newPath[0]
            self.dirs[path[0]].addDir(name, newPath)
    def getDir(self, name):
        return self.dirs.get(name)
    def getSize(self):
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.dirs.values():
            size += dir.getSize()
        return size
    def flatmapDirs(self):
        dirs = []
        dirs += self.dirs.values()
        for dir in self.dirs.values():
            dirs += dir.flatmapDirs()
        return dirs
    def toString(self, nested = 0):
        stringBuilder = ""
        tabAppender = ""
        for i in range(nested):
            tabAppender += "\t"
        stringBuilder += f"- {self.name} (dir)\n"
        for file in self.files:
            stringBuilder += f"{tabAppender}\t- {file.name} (file, size={file.size})\n"
        for dir in self.dirs.values():
            stringBuilder += f"{tabAppender}\t{dir.toString(nested + 1)}"
        return stringBuilder


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __str__(self) -> str:
        return f"({self.name} {self.size})"

class pathTracker():
    def __init__(self):
        self.pathArray = []
    def __len__(self):
        return len(self.pathArray)
    def apppendPath(self, path):
        self.pathArray.append(path)
    def popPath(self):
        return self.pathArray.pop()
    def toString(self):
        stringBuilder = "/"
        for item in self.pathArray:
            stringBuilder += item
            if (item != self.pathArray[-1:][0]):
                stringBuilder += "/"
        return stringBuilder

def getMaxSizeDirs(dir: Dir):
    selectedDirs = []
    if dir.getSize() <= 100000:
        selectedDirs.append(dir)
    if len(dir.dirs) > 0:
        for nestedDir in dir.dirs.values():
            selectedDirs += getMaxSizeDirs(nestedDir)

    return selectedDirs

def processCommands(filePath):
    currentPath = pathTracker();
    dataStructure = Dir("/")
    lsReadMode = False
    for command in open(filePath).readlines():
        if "$ cd" in command:
            lsReadMode = False
            dirLocation = command[5:].replace("\n", "")
            if (dirLocation == ".."):
                currentPath.popPath()
            elif (dirLocation != "/"):
                currentPath.apppendPath(dirLocation)
            print(f"Path is: {currentPath.toString()}")
        if "$ ls" in command:
            lsReadMode = True
            continue
        if lsReadMode:
                if "dir" in command:
                    dirName = command.replace("\n", "").split(" ")[1]
                    dataStructure.addDir(dirName, currentPath.pathArray)
                else:
                    fileSize, fileName = command.replace("\n", "").split(" ")
                    file = File(fileName, int(fileSize))
                    dataStructure.addFile(file, currentPath.pathArray)
    totalDiskSpace = 70000000
    totalUsedSpace = dataStructure.getSize()
    totalNeededSpace = 30000000
    spaceToFreeUp = totalNeededSpace - (totalDiskSpace - totalUsedSpace)
    print(f"total space to free up: {spaceToFreeUp}")

    closestDir = None
    closestDelta = math.inf
    allDirs = dataStructure.flatmapDirs()
    for dir in allDirs:
        size = dir.getSize()
        if size < spaceToFreeUp:
            continue
        delta = math.fabs(spaceToFreeUp - size)
        print(f"Dir: {dir.name}\t Size: {size}\t Delta: {delta}")
        if (delta < closestDelta):
            closestDelta = delta
            closestDir = dir
    print(f"dir: {closestDir.name} size: {closestDir.getSize()}")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processCommands(filePath)