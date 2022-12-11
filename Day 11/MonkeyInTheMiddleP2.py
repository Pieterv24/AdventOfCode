import sys
from os import path

class Monkey(object):
    def __init__(self, number, items, operation, test, division):
        self.number = number
        self.items = items
        self.operation = operation
        self.division = division
        self.test = test
        self.inspections = 0

    def canInspect(self):
        return len(self.items) > 0

    def inspect(self):
        # print(f"Monkey inspects item of level {self.items[0]}")
        self.items[0] = self.operation(self.items[0])
        self.inspections += 1
        # print(f"New worry level is: {self.items[0]}")

    def bored(self, mod):
        # print(f"Monkey gets bored with item new level is: {int(self.items[0]/3)}")
        self.items[0] %= mod

    def throw(self):
        item = self.items[0]
        self.items.remove(item)
        return (self.test(item), item)

    def acceptThrow(self, item):
        self.items.append(item)

def monkeyTest(value, division, trueMonkey, falseMonkey):
    if value % division == 0:
        return trueMonkey
    else:
        return falseMonkey

def createMonkey(buffer):
    _, monkeyNumber = buffer[0].replace(":", "").split(" ")
    monkeyNumber = int(monkeyNumber)
    _, itemString = buffer[1].split(": ")
    items = []
    for i in itemString.split(", "):
        items.append(int(i))
    # Get operation lambda
    _, operation = buffer[2].split("= ")
    if "*" in operation:
        _, arg = operation.split("*")
        if "old" in arg:
            operation = lambda val : val * val
        else:
            operation = lambda val : val * int(arg)
    elif "+" in operation:
        _, arg = operation.split("+")
        if "old" in arg:
            operation = lambda val : val + val
        else:
            operation = lambda val : val + int(arg)
    # Create test lambda
    division = int(buffer[3].split(" ")[3])
    trueMonkey = int(buffer[4].split(" ")[5])
    falseMonkey = int(buffer[5].split(" ")[5])
    
    test = lambda input : monkeyTest(input, division, trueMonkey, falseMonkey)

    return Monkey(monkeyNumber, items, operation, test, division)

def readMonkeys(fileLines):
    monkeys = []
    buffer = []
    for line in fileLines:
        if line == "\n":
            monkeys.append(createMonkey(buffer))
            buffer = []
        else:
            buffer.append(line.replace("\n", "").strip())
    monkeys.append(createMonkey(buffer))

    return monkeys

def processFile(filePath):
    fileContent = open(filePath).readlines()
    
    mod = 1
    rounds = 10000
    monkeys = readMonkeys(fileContent)
    for monkey in monkeys:
        mod = (mod*monkey.division)

    for round in range(rounds):
        print(f"Round: {round}")
        for monkey in monkeys:
            print(f"Monkey: {monkey.number}")
            while (monkey.canInspect()):
                monkey.inspect()
                monkey.bored(mod)
                (target, value) = monkey.throw()
                # print(f"Item with value: {value} is thrown to {target}")
                monkeys[target].acceptThrow(value)

    inspectionCounts = []
    for monkey in monkeys:
        print(f"Monkey {monkey.number} did {monkey.inspections} inspections")
        inspectionCounts.append(monkey.inspections)

    inspectionCounts.sort(reverse=True)
    print(f"Answer is: {inspectionCounts[0] * inspectionCounts[1]}")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Please select file to read")
        exit()
    if (path.exists(sys.argv[1])):
        filePath = sys.argv[1]
        print(f"Processing {filePath}...")
        processFile(filePath)