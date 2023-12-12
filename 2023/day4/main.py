with open('2023/day4/input.txt') as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    card, numbers = line.split(': ')
    winning_numbers, my_numbers = numbers.split(' | ')
    winning_numbers = {int(num) for num in winning_numbers.split()}
    my_numbers = {int(num) for num in my_numbers.split()}
    intersection = winning_numbers.intersection(my_numbers)
    result += 2**(len(intersection)-1) if len(intersection) > 0 else 0
print(result)


result = 0
dictt = {f'Card {i+1}': 1 for i in range(len(lines))}
for i, line in enumerate(lines):
    card, numbers = line.split(': ')
    winning_numbers, my_numbers = numbers.split(' | ')
    winning_numbers = {int(num) for num in winning_numbers.split()}
    my_numbers = {int(num) for num in my_numbers.split()}
    intersection = winning_numbers.intersection(my_numbers)
    for j in range(len(intersection)):
        dictt[f'Card {i+j+2}'] += dictt[f'Card {i+1}']
print(sum(dictt.values()))
