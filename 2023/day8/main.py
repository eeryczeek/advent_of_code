from itertools import cycle
import math
with open("2023/day8/input.txt") as f:
    lines = f.read().splitlines()

graph = {}


graph = {origin: tuple(destinations.strip("()").split(", "))
         for origin, destinations in (line.split(" = ") for line in lines[2:])}


counter = 0
origin = 'AAA'
for direction in cycle(lines[0]):
    if origin == 'ZZZ':
        break
    counter += 1
    origin = graph[origin][0] if direction == 'L' else graph[origin][1]

print(counter)

counters = []
origins = [x for x in graph.keys() if x.endswith('A')]
destinations = [x for x in graph.keys() if x.endswith('Z')]
for origin in origins:
    original_origin = origin
    counter = 0
    old_counter = None
    for direction in cycle(lines[0]):
        if origin in destinations:
            counters.append(counter)
            break
        counter += 1
        origin = graph[origin][0] if direction == 'L' else graph[origin][1]
print(math.lcm(*counters))
