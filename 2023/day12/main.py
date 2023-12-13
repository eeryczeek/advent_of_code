
with open("2023/day12/input.txt") as f:
    lines = f.read().splitlines()


def generate_all_possible_arrangements(onsens: str, numbers: list):
    strings = []
    for number in range(2 ** onsens.count("?")):
        binary = bin(number)[2:]
        binary = "0" * (onsens.count("?") - len(binary)) + binary
        string = onsens
        for char in binary:
            string = string.replace("?", '.' if char == '1' else '#', 1)
        strings.append(string)
    return strings


listt = ['0.23', '0.44', '1.7', '1', '2.0']
print([float(x).is_integer() for x in listt])


result = 0
for line in lines:
    onsens = line.split(" ")[0]
    numbers = [int(x) for x in line.split(" ")[1].split(",")]
    for string in generate_all_possible_arrangements(onsens, numbers):
        numbers_check = [x.count('#')
                         for x in string.split(".") if x.count('#') > 0]
        if numbers_check == numbers:
            result += 1
print(result)


result = 0
for line in lines:
    print(result)
    onsens = line.split(" ")[0]
    onsens = [onsens for i in range(5)]
    onsens = "?".join(onsens)
    numbers = [int(x) for x in line.split(" ")[1].split(",")]
    numbers = [numbers for i in range(5)]
    numbers = [x for sublist in numbers for x in sublist]
    print(onsens)
    print(numbers)
    for string in generate_all_possible_arrangements(onsens):
        numbers_check = [x.count('#')
                         for x in string.split(".") if x.count('#') > 0]
        if numbers_check == numbers:
            result += 1
print(result)
