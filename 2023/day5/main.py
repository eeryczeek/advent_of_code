import time


with open('2023/day5/input.txt') as f:
    lines = f.readlines()


def get_destination_from_source(lines, converter_name: str, source: str):
    indexx = lines.index(f'{converter_name} map:\n')
    for line in lines[indexx + 1:]:
        if line == '\n':
            return source
        if int(line.split()[1]) <= int(source) < int(line.split()[1]) + int(line.split()[2]):
            return str(int(line.split()[0]) + int(source) - int(line.split()[1]))
    return source


destinations = []
for source in lines[0].split(': ')[1].split():
    for converter in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        source = get_destination_from_source(lines, converter, source)
    destinations.append(source)
print(min([int(x) for x in destinations]))


def get_conversions(lines):
    conversions = {}
    for i, line in enumerate(lines[1:]):
        if line.endswith('map:\n'):
            converter_name = line.split()[0]
            conversions[converter_name] = []
            for j, line in enumerate(lines[i + 2:]):
                if line == '\n':
                    break
                conversions[converter_name].append(((int(line.split()[1]), int(line.split()[1]) + int(
                    line.split()[2])), (int(line.split()[0]), int(line.split()[0]) + int(line.split()[2]))))
            for key, value in conversions.items():
                value.sort()
                conversions[key] = value
    return conversions


starting_seeds = [int(x) for x in lines[0].split(': ')[1].split()]
starting_seeds = sorted([(starting_seed1, starting_seed1 + seed_range)
                         for starting_seed1, seed_range in zip(starting_seeds[:-1:2], starting_seeds[1::2])])


def merge_ranges(ranges):
    ranges.sort()
    result = [ranges[0]]
    for current in ranges[1:]:
        last = result[-1]
        if current[0] <= last[1]:
            result[-1] = (last[0], max(last[1], current[1]))
        else:
            result.append(current)
    return result


for converter_name, conversions in get_conversions(lines).items():
    new_starting_seeds = []
    for i, (left, right) in enumerate(starting_seeds):
        changed = False
        for ((source_left, source_right), (destination_left, destination_right)) in conversions:
            if source_left <= left < source_right or source_left < right <= source_right:
                changed = True
                if source_left <= left < source_right and source_left < right <= source_right:
                    new_starting_seeds.append(
                        (destination_left + left - source_left, destination_left + right - source_left))
                if source_left <= left < source_right and not source_left < right <= source_right:
                    starting_seeds.append((source_right, right))
                    new_starting_seeds.append(
                        (destination_left + left - source_left, destination_right))
                if not source_left <= left < source_right and source_left < right <= source_right:
                    starting_seeds.append((left, source_left))
                    new_starting_seeds.append(
                        (destination_left, destination_left + right - source_left))
                if not source_left <= left < source_right and not source_left < right <= source_right:
                    starting_seeds.append((left, source_left))
                    starting_seeds.append((source_right, right))
                    new_starting_seeds.append(
                        (destination_left, destination_right))
        if not changed:
            new_starting_seeds.append((left, right))
    starting_seeds = new_starting_seeds
    starting_seeds = merge_ranges(sorted(starting_seeds))


print(sorted(starting_seeds)[0][0])
