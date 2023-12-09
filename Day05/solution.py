f = open("input.txt", "r")

seeds = [int(seed) for seed in f.readline().split() if seed.isdigit()]
almanac = [line.strip() for line in f.readlines() if line != '\n']
instructions = []
newInstruction = []
for entry in almanac:
    if not entry[0].isdigit():
        instructions.append(newInstruction)
        newInstruction = []
    else:
        newInstruction.append(tuple([int(number) for number in entry.split()]))
instructions.append(newInstruction)
instructions.pop(0)
locations = []

def createMap(instructionGroup, seed):
    for inst in instructionGroup:
        destination, source, mapRange = inst
        if source <= seed and source + mapRange >= seed:
            newSeed = destination + (seed - source)
            break
        else:
            newSeed = seed
    return newSeed

for seed in seeds:
    newSeed = seed
    for instruction in instructions:
        newSeed = createMap(instruction, newSeed)
    locations.append(newSeed)

print(f"Part 1: {min(locations)}")