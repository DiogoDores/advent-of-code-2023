f = open("input.txt", "r")
input = [line for line in f.readlines()]

def data_calibration(input):
    calibrationValues = []
    for line in input:
        if not line.strip().isalpha():
            calibrationValues.append(int(''.join([[digit for digit in line if digit.isdigit()][0], [digit for digit in line[::-1] if digit.isdigit()][0]])))
    return calibrationValues

print(f'Part 1: {sum(data_calibration(input))}')

input = [line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine") for line in input]

print(f'Part 2: {sum(data_calibration(input))}')