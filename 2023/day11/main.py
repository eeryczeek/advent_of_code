with open("2023/day11/input.txt", 'r') as f:
    lines = f.read().splitlines()

for difference in [1, 999_999]:
    empty_row_indexes = {y for y, line in enumerate(lines) if '#' not in line}
    empty_col_indexes = {x for x in range(len(lines[0])) if all(
        lines[y][x] != '#' for y in range(len(lines)))}
    galaxies = [(y, x) for y in range(len(lines))
                for x in range(len(lines[0])) if lines[y][x] == '#']

    result = sum(abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
                 for i, galaxy1 in enumerate(galaxies) for j, galaxy2 in enumerate(galaxies) if i < j)
    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i:]:
            result += sum(difference for empty_row_index in empty_row_indexes
                          if min(galaxy1[0], galaxy2[0]) < empty_row_index < max(galaxy1[0], galaxy2[0]))
            result += sum(difference for empty_col_index in empty_col_indexes
                          if min(galaxy1[1], galaxy2[1]) < empty_col_index < max(galaxy1[1], galaxy2[1]))
    print(result)
