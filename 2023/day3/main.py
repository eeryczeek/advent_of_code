from itertools import product
# part 1:
with open('2023/day3/input.txt') as f:
    lines = f.readlines()

mask1 = [[1 if char != '\n' and char != '.' and not char.isnumeric() else 0 for char in line]
         for line in lines]

valid_numbers = {(i_, j_) for i, line in enumerate(mask1) for j, char in enumerate(line) if char == 1 for i_, j_ in product(
    range(i - 1, i + 2), range(j - 1, j + 2)) if 0 <= i_ < len(mask1) and 0 <= j_ < len(mask1[0]) and mask1[i_][j_] == 0}

already_checked = set()
result = 0
for i, j in valid_numbers:
    if lines[i][j].isdigit() and (i, j) not in already_checked:
        number = ''
        k = 0
        while lines[i][j+k].isdigit():
            already_checked.add((i, j+k))
            number += lines[i][j+k]
            k += 1
        k = 1
        while lines[i][j-k].isdigit():
            already_checked.add((i, j-k))
            number = lines[i][j-k] + number
            k += 1
        result += int(number)
print(result)


# part 2:

mask2 = [[1 if char == '*' else 0 for char in line] for line in lines]

valid_numbers = {(i_, j_, i, j): [] for i, line in enumerate(mask2) for j, char in enumerate(line) if char == 1
                 for i_, j_ in product(range(i - 1, i + 2), range(j - 1, j + 2))
                 if 0 <= i_ < len(mask2) and 0 <= j_ < len(mask2[0]) and mask2[i_][j_] == 0}

gears = {(i, j): [] for i, line in enumerate(mask2)
         for j, char in enumerate(line) if char == 1}

already_checked = set()
for i, j, g_i, g_j in valid_numbers:
    if lines[i][j].isdigit() and (i, j) not in already_checked:
        number = ''
        k = 0
        while lines[i][j+k].isdigit():
            already_checked.add((i, j+k))
            number += lines[i][j+k]
            k += 1
        k = 1
        while lines[i][j-k].isdigit():
            already_checked.add((i, j-k))
            number = lines[i][j-k] + number
            k += 1
        gears[(g_i, g_j)].append(int(number))

result = 0
for key, values in gears.items():
    if len(values) == 2:
        starting_value = values[0]
        for value in values[1:]:
            starting_value *= value
        result += starting_value
print(result)
