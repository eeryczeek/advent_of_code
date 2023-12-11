with open("2023/day10/input.txt") as f:
    lines = f.read().splitlines()

start = next(((i, line.find('S'))
              for i, line in enumerate(lines) if 'S' in line), None)
lines = [list(line) for line in lines]

y, x = start
if 0 <= y-1 and y+1 < len(lines):
    if lines[y-1][x] in ['|', 'F', '7'] and lines[y+1][x] in ['|', 'L', 'J']:
        lines[y][x] = '|'
if 0 <= x-1 and x+1 < len(lines[0]):
    if lines[y][x-1] in ['-', 'F', 'L'] and lines[y][x+1] in ['-', 'J', '7']:
        lines[y][x] = '-'
if 0 <= y-1 and 0 <= x-1:
    if lines[y-1][x] in ['|', 'F', '7'] and lines[y][x-1] in ['-', 'F', 'L']:
        lines[y][x] = 'J'
if 0 <= y-1 and x+1 < len(lines[0]):
    if lines[y-1][x] in ['|', 'F', '7'] and lines[y][x+1] in ['-', 'J', '7']:
        lines[y][x] = 'L'
if y+1 < len(lines) and 0 <= x-1:
    if lines[y+1][x] in ['|', 'L', 'J'] and lines[y][x-1] in ['-', 'F', 'L']:
        lines[y][x] = '7'
if y+1 < len(lines) and x+1 < len(lines[0]):
    if lines[y+1][x] in ['|', 'L', 'J'] and lines[y][x+1] in ['-', 'J', '7']:
        lines[y][x] = 'F'

loop = {start}
queue = [(start, 0)]
while queue:
    (y, x), cost = queue.pop(0)
    for direction, (dy, dx) in {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}.items():
        nexty, nextx = y + dy, x + dx
        if 0 <= nexty < len(lines) and 0 <= nextx < len(lines[0]):
            match direction:
                case 'up':
                    if lines[y][x] in ['|', 'L', 'J'] and lines[nexty][nextx] in ['|', 'F', '7']:
                        if (nexty, nextx) not in loop:
                            loop.add((nexty, nextx))
                            queue.append(((nexty, nextx), cost + 1))
                case 'down':
                    if lines[y][x] in ['|', 'F', '7'] and lines[nexty][nextx] in ['|', 'L', 'J']:
                        if (nexty, nextx) not in loop:
                            loop.add((nexty, nextx))
                            queue.append(((nexty, nextx), cost + 1))
                case 'left':
                    if lines[y][x] in ['-', 'J', '7'] and lines[nexty][nextx] in ['-', 'F', 'L']:
                        if (nexty, nextx) not in loop:
                            loop.add((nexty, nextx))
                            queue.append(((nexty, nextx), cost + 1))
                case 'right':
                    if lines[y][x] in ['-', 'F', 'L'] and lines[nexty][nextx] in ['-', 'J', '7']:
                        if (nexty, nextx) not in loop:
                            loop.add((nexty, nextx))
                            queue.append(((nexty, nextx), cost + 1))

print(cost)


for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y, x) not in loop:
            lines[y][x] = '.'

lines_dilated = [" ".join(line) for line in lines]
lines_dilated = ["".join(line) for line in zip(*lines_dilated)]
lines_dilated = [" ".join(line) for line in lines_dilated]
lines_dilated = ["".join(line) for line in zip(*lines_dilated)]
lines_dilated = [" " + line + " " for line in lines_dilated]
lines_dilated = [" " * len(lines_dilated[0])] + \
    lines_dilated + [" " * len(lines_dilated[0])]


lines_dilated = [list(line) for line in lines_dilated]
for y in range(len(lines_dilated)):
    for x in range(len(lines_dilated[0])):
        if lines_dilated[y][x] == ' ':
            if 0 <= y-1 and y+1 < len(lines_dilated):
                if lines_dilated[y-1][x] in ['|', 'F', '7'] and lines_dilated[y+1][x] in ['|', 'L', 'J']:
                    lines_dilated[y][x] = '|'
            if 0 <= x-1 and x+1 < len(lines_dilated[0]):
                if lines_dilated[y][x-1] in ['-', 'F', 'L'] and lines_dilated[y][x+1] in ['-', 'J', '7']:
                    lines_dilated[y][x] = '-'
            if 0 <= y-1 and 0 <= x-1:
                if lines_dilated[y-1][x] in ['|', 'F', '7'] and lines_dilated[y][x-1] in ['-', 'F', 'L']:
                    lines_dilated[y][x] = 'J'
            if 0 <= y-1 and x+1 < len(lines_dilated[0]):
                if lines_dilated[y-1][x] in ['|', 'F', '7'] and lines_dilated[y][x+1] in ['-', 'J', '7']:
                    lines_dilated[y][x] = 'L'
            if y+1 < len(lines_dilated) and 0 <= x-1:
                if lines_dilated[y+1][x] in ['|', 'L', 'J'] and lines_dilated[y][x-1] in ['-', 'F', 'L']:
                    lines_dilated[y][x] = '7'
            if y+1 < len(lines_dilated) and x+1 < len(lines_dilated[0]):
                if lines_dilated[y+1][x] in ['|', 'L', 'J'] and lines_dilated[y][x+1] in ['-', 'J', '7']:
                    lines_dilated[y][x] = 'F'


lines_dilated = ["".join(line) for line in lines_dilated]


def bfs(y, x):
    visited = set()
    tiles = set()
    queue = [(y, x)]
    while queue:
        y, x = queue.pop(0)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nexty, nextx = y + dy, x + dx
            if 0 <= nexty < len(lines_dilated) and 0 <= nextx < len(lines_dilated[0]):
                if lines_dilated[nexty][nextx] in ['.', ' ']:
                    if (nexty, nextx) not in visited:
                        visited.add((nexty, nextx))
                        queue.append((nexty, nextx))
                        if lines_dilated[nexty][nextx] == '.':
                            tiles.add((nexty, nextx))
    return tiles


print(sum(line.count('.') for line in lines_dilated) - len(bfs(0, 0)))

with open("2023/day10/output.txt", 'w') as f:
    f.write('\n'.join(lines_dilated))
