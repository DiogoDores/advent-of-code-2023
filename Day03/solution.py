f = open("input.txt", "r")
input = [line.strip() for line in f.readlines()]
symbols = set()
gears = []
numbers = []
numberCreation = False
numberString = ""
partNumberSum = 0
gearRatioSum = 0

def generateNumberCoordinates(x1, x2, y):
    coords = [(x1, y)]
    for x in range(x1 + 1, x2 + 1):
        coords.append((x, y))
    return coords

def generateSymbolNeighbourCoordinates(x, y):
    symbols.add((x - 1, y - 1))
    symbols.add((x, y - 1))
    symbols.add((x + 1, y - 1))
    symbols.add((x - 1, y))
    symbols.add((x, y))
    symbols.add((x + 1, y))
    symbols.add((x - 1, y + 1))
    symbols.add((x, y + 1))
    symbols.add((x + 1, y + 1))

def generateGearNeighbourCoordinates(x, y):
    gears.append({(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                  (x - 1, y), (x, y), (x + 1, y),
                  (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)})

for y, line in enumerate(input):
    numberX1 = -1
    for x, symbol in enumerate(line):
        if not symbol.isdigit() and symbol != '.':
            generateSymbolNeighbourCoordinates(x, y)
            if symbol == '*':
                generateGearNeighbourCoordinates(x, y)
        if symbol.isdigit():
            if not numberCreation:
                numberCreation = True
                numberX1 = x
            numberString += symbol
            if numberCreation and x == len(line) - 1:
                numberCreation = False
                numbers.append({int(numberString): generateNumberCoordinates(numberX1, x, y)})
                numberString = ""
        elif not symbol.isdigit() and numberCreation:
            numberCreation = False
            numbers.append({int(numberString): generateNumberCoordinates(numberX1, x - 1, y)})
            numberString = ""

for number in numbers:
    for number, coords in number.items():
        if(bool(symbols & set(coords))):
            partNumberSum += number

for gear in gears:
    matches = []
    for number in numbers:
        for number, coords in number.items():
            if(bool(gear & set(coords))):
                matches.append(number)
    if len(matches) == 2:
        gearRatioSum += matches[0] * matches[1]

print(f"Part 1: {partNumberSum}")
print(f"Part 2: {gearRatioSum}")