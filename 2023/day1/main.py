part1 = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


part2 = {
    '1': 1,
    'one': 1,
    '2': 2,
    'two': 2,
    '3': 3,
    'three': 3,
    '4': 4,
    'four': 4,
    '5': 5,
    'five': 5,
    '6': 6,
    'six': 6,
    '7': 7,
    'seven': 7,
    '8': 8,
    'eight': 8,
    '9': 9,
    'nine': 9,
}

for digits in [part1, part2]:
    result = 0
    with open('2023/day1/input.txt') as f:
        for line in f:
            all_substrings = [digits[line[i:j]]
                              for i in range(len(line)-1) for j in range(i + 1, min(len(line), i+6)) if line[i:j] in digits.keys()]
            print(all_substrings)
            result += 10 * all_substrings[0] + all_substrings[-1]
    print(result)
