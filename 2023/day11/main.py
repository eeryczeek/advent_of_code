with open("2023/day11/input.txt", 'r') as f:
    lines = f.read().splitlines()

output = []
for line in lines:
    if '#' not in line:
        output.append(line)
        output.append(line)
    else:
        output.append(line)

lines = ["".join(line) for line in zip(*output)]

output = []
for line in lines:
    if '#' not in line:
        output.append(line)
        output.append(line)
    else:
        output.append(line)

lines = ["".join(line) for line in zip(*output)]

galaxies = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            galaxies.add((y, x))

result = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            result += abs(galaxy1[0] - galaxy2[0]) + \
                abs(galaxy1[1] - galaxy2[1])
print(result//2)


with open("2023/day11/input.txt", 'r') as f:
    lines = f.read().splitlines()

empty_row_indexes = [i for i, line in enumerate(lines) if '#' not in line]
empty_col_indexes = [i for i, line in enumerate(
    zip(*lines)) if '#' not in line]

print(empty_row_indexes)
print(empty_col_indexes)

galaxies = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            galaxies.add((y, x))

result = 0
for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 != galaxy2:
            result += abs(galaxy1[0] - galaxy2[0]) + \
                abs(galaxy1[1] - galaxy2[1])
            for empty_row_index in empty_row_indexes:
                if galaxy1[0] < empty_row_index < galaxy2[0] or galaxy2[0] < empty_row_index < galaxy1[0]:
                    result += 1_000_000
            for empty_col_index in empty_col_indexes:
                if galaxy1[1] < empty_col_index < galaxy2[1] or galaxy2[1] < empty_col_index < galaxy1[1]:
                    result += 1_000_000
print(result//2)
