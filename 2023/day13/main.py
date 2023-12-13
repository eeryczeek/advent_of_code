with open("2023/day13/input.txt") as f:
    patterns = [list(line.split('\n'))
                for line in ''.join(f.readlines()).split('\n\n')]


def find_symmetry_index(pattern: list, already_found: int = None):
    return next((row for row in range(1, len(pattern)) if all(line1 == line2 for line1, line2 in zip(pattern[:row][::-1], pattern[row:])) and row != already_found), None)


def alter_pattern(pattern: list):
    for y, line in enumerate(pattern):
        for x, char in enumerate(line):
            changed_pattern = [list(line) for line in pattern]
            changed_pattern[y][x] = '#' if char == '.' else '.'
            yield ["".join(line) for line in changed_pattern]


rows1, columns1, rows2, columns2 = 0, 0, 0, 0
for pattern in patterns:
    pattern_t = ["".join(line) for line in zip(*pattern)]
    rows1 += find_symmetry_index(pattern) or 0
    columns1 += find_symmetry_index(pattern_t) or 0
    for altered_pattern in alter_pattern(pattern):
        if find_symmetry_index(altered_pattern, find_symmetry_index(pattern)):
            rows2 += find_symmetry_index(altered_pattern,
                                         find_symmetry_index(pattern))
            break

        altered_pattern_t = ["".join(line) for line in zip(*altered_pattern)]
        if find_symmetry_index(altered_pattern_t, find_symmetry_index(pattern_t)):
            columns2 += find_symmetry_index(altered_pattern_t,
                                            find_symmetry_index(pattern_t))
            break
print(rows1 * 100 + columns1)
print(rows2 * 100 + columns2)
