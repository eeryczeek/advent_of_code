import itertools


with open("2023/day13/input.txt") as f:
    lines = f.readlines()

patterns = [list(g) for k, g in itertools.groupby(
    lines, key=lambda x: x != '\n') if k]

rows, columns = 0, 0
for pattern in patterns:
    pattern = [line.strip('\n') for line in pattern]
    rows += sum(row for row in range(1, len(pattern)) if all(line1 ==
                line2 for line1, line2 in zip(pattern[:row][::-1], pattern[row:])))

    pattern = ["".join(line) for line in zip(*pattern)]
    columns += sum(column for column in range(1, len(pattern)) if all(line1 ==
                   line2 for line1, line2 in zip(pattern[:column][::-1], pattern[column:])))
print(rows * 100 + columns)


def alter_pattern(pattern: list):
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            changed_pattern = [list(line) for line in pattern]
            changed_pattern[y][x] = '#' if changed_pattern[y][x] == '.' else '.'
            yield ["".join(line) for line in changed_pattern]


rows, columns = 0, 0
for pattern in patterns:
    pattern = [line.strip('\n') for line in pattern]
    for altered_pattern in alter_pattern(pattern):
        for row in range(1, len(altered_pattern)):
            if all(line1 == line2 for line1, line2 in zip(altered_pattern[:row][::-1], altered_pattern[row:])):
                rows += row

        altered_pattern = ["".join(line) for line in zip(*altered_pattern)]
        for column in range(1, len(altered_pattern)):
            if all(line1 == line2 for line1, line2 in zip(altered_pattern[:column][::-1], altered_pattern[column:])):
                columns += column

print(rows * 100 + columns)
