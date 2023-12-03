cube_limits1 = {'red': 12, 'green': 13, 'blue': 14}
result = 0
with open('2023/day2/input.txt') as f:
    for line in f:
        game, sets = line[:-1].split(': ')
        _, game_id = game.split(' ')
        sets = [set_.split(', ') for set_ in sets.split('; ')]
        result += int(game_id) if all([int(number) <= cube_limits1[color]
                                       for set_ in sets for cube in set_ for number, color in [cube.split(' ')]]) else 0

print(result)


def update_min_values(min_values, cube):
    number, color = cube.split(' ')
    min_values[color] = max(min_values[color], int(number))
    return min_values


result = 0
with open('2023/day2/input.txt') as f:
    for line in f:
        game, sets = line[:-1].split(': ')
        sets = [set_.split(', ') for set_ in sets.split('; ')]
        _, game_id = game.split(' ')
        min_values = {'red': 0, 'green': 0, 'blue': 0}
        for set_ in sets:
            for cube in set_:
                min_values = update_min_values(min_values, cube)
        result += min_values['red'] * min_values['green'] * min_values['blue']

print(result)
