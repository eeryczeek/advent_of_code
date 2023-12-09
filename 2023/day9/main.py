with open("2023/day9/input.txt") as f:
    lines = f.read().splitlines()

result1, result2 = 0, 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    differences = [numbers]
    while not all(x == 0 for x in numbers):
        numbers = [j - i for i, j in zip(numbers, numbers[1:])]
        differences.append(numbers)
    result1 += sum(difference[-1] for difference in differences)
    result2 += sum(difference[::-1][-1] if i % 2 == 0 else -difference[::-1][-1]
                   for i, difference in enumerate(differences))
print(result1)
print(result2)
