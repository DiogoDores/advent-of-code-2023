f = open("input.txt", "r")
input = [line for line in f.readlines()]
totalPoints = 0
cardCount = [1] * (len(input))

for i, line in enumerate(input):
    winningNumbers = [int(line) for line in line[line.find(':') + 1:line.find('|')].split()]
    myNumbers = [int(line) for line in line[line.find('|') + 1:].strip().split()]
    matches = list(set(winningNumbers) & set(myNumbers))
    if len(matches) > 0:
        totalPoints += pow(2, len(matches) - 1)
    for j in range(i + 1, i + len(matches) + 1):
        cardCount[j] += 1 * cardCount[i]

print(f"Part 1: {totalPoints}")
print(f"Part 2: {sum(cardCount)}")