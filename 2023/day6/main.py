with open("2023/day6/input.txt") as f:
    lines = f.read().splitlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]


def try_all_times(time, distance):
    result = 0
    for holding_time in range(time+1):
        if holding_time * (time-holding_time) > distance:
            result += 1
    return result


summ = 1
for time, distance in zip(times, distances):
    summ *= try_all_times(time, distance)
print(summ)


time = int("".join(lines[0].split(":")[1].split()))
distance = int("".join(lines[1].split(":")[1].split()))


def try_all_times(time, distance):
    result = 0
    for holding_time in range(time+1):
        if holding_time * (time-holding_time) > distance:
            result += 1
    return result


print(try_all_times(time, distance))
