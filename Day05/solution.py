import functools
f = open("input.txt", "r")

seeds = [int(seed) for seed in f.readline().split() if seed.isdigit()]
almanac = [line.strip() for line in f.readlines() if line != '\n']
locations = []
seedToSoil, soilToFertilizer, fertilizerToWater = {}, {}, {}
waterToLight, lightToTemperature, temperatureToHumidity = {}, {}, {}
humidityToLocation = {}

def getLocation(seed):
    soil = seedToSoil[seed] if seed in seedToSoil.keys() else seed
    fertilizer = soilToFertilizer[soil] if soil in soilToFertilizer.keys() else soil
    water = fertilizerToWater[fertilizer] if fertilizer in fertilizerToWater.keys() else fertilizer
    light = waterToLight[water] if water in waterToLight.keys() else water
    temperature = lightToTemperature[light] if light in lightToTemperature.keys() else light
    humidity = temperatureToHumidity[temperature] if temperature in temperatureToHumidity.keys() else temperature
    location = humidityToLocation[humidity] if humidity in humidityToLocation.keys() else humidity
    locations.append(location)

def createMap(entry, mapper):
    destination, source, mapRange = [int(number) for number in entry.split()]
    for i in range(mapRange):
        mapper[source + i] = destination + i

for entry in almanac:
    if 'seed-to-soil' in entry:
        mapper = seedToSoil
    elif 'soil-to-fertilizer' in entry:
        mapper = soilToFertilizer
    elif 'fertilizer-to-water' in entry:
        mapper = fertilizerToWater
    elif 'water-to-light' in entry:
        mapper = waterToLight
    elif 'light-to-temperature' in entry:
        mapper = lightToTemperature
    elif 'temperature-to-humidity' in entry:
        mapper = temperatureToHumidity
    elif 'humidity-to-location' in entry:
        mapper = humidityToLocation
    elif entry[0].isdigit():
        createMap(entry, mapper)

for seed in seeds:
    getLocation(seed)

print(f"Part 1: {functools.reduce(lambda a, b: a if a < b else b, locations)}")