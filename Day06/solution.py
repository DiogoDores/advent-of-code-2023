import math

f = open("input.txt", "r")
t = f.readline().strip().split(':')[1].split()
r = f.readline().strip().split(':')[1].split()
times = list(map(int, t))
records = list(map(int, r))
singleRaceTime = [int(''.join(t))]
singleRaceRecord = [int(''.join(r))]

def calculate_win_times(raceTime, allRecords):
    allDistances, wins = [], []
    res = 1
    for time in raceTime:
        travelledDistances = []
        for t in range(1, math.ceil(time)):
            travelledDistances.append(t * (time - t))
        allDistances.append(travelledDistances)

    for i, distances in enumerate(allDistances):
        occur = 0
        for distance in distances:
            if distance > allRecords[i]:
                occur += 1
        wins.append(occur)

    for win in wins: res *= win
    return res

print(f"Part 1: {calculate_win_times(times, records)}")
print(f"Part 2: {calculate_win_times(singleRaceTime, singleRaceRecord)}")