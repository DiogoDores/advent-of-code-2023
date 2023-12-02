f = open("input.txt", "r")
cubes = {'red': 12, 'green': 13, 'blue': 14}
games = []
idSum = 0
totalPower = 0

def cubes_per_set(set):
    setList = set.replace(',', '').split()
    return [{'red':int(setList[setList.index('red') - 1])} if 'red' in setList else {'red': 0},
            {'green':int(setList[setList.index('green') - 1])} if 'green' in setList else {'green': 0},
            {'blue':int(setList[setList.index('blue') - 1])} if 'blue' in setList else {'blue': 0}]

for line in f.readlines():
    game = []
    semiColonIndexes = [i for i, char in enumerate(line) if char == ';']
    game += cubes_per_set(line[line.find(':') + 2:semiColonIndexes[0]])
    for i, index in enumerate(semiColonIndexes):
        if i + 1 >= len(semiColonIndexes):
            break
        game += cubes_per_set(line[index + 2:semiColonIndexes[i+1]])
    game += cubes_per_set(line[semiColonIndexes[-1] + 2:])
    
    games.append(game)

for index, game in enumerate(games):
    occur = 0
    totalPower += max(item['red'] for item in game if item.get('red'))  \
                    * max(item['green'] for item in game if item.get('green')) \
                    * max(item['blue'] for item in game if item.get('blue'))
    for set in game:
        for color, number in set.items():
            if number <= cubes[color]:
                occur += 1
    if occur == len(game):
        idSum += index + 1

print(f"Part 1: {idSum}")
print(f"Part 2: {totalPower}")

    