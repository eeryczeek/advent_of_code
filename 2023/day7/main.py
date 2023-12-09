import itertools


class CamelCards:
    def __init__(self):
        self.card_values1 = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                             "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
                             "Q": 12, "K": 13, "A": 14}

        self.card_values2 = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                             "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
                             "Q": 12, "K": 13, "A": 14}

        self.hand_types = [self.is_five_of_a_kind, self.is_four_of_a_kind, self.is_full_house,
                           self.is_three_of_a_kind, self.is_two_pairs, self.is_one_pair, self.is_high_card]

    def get_value_for_highest_type(self, hand):
        for i, func in enumerate(self.hand_types):
            if func(hand):
                if i == len(self.hand_types) - 1:
                    return 14 ** 5
                return (len(self.hand_types) - i) * (14 ** 6)
        return 0

    def is_five_of_a_kind(self, hand):
        return len(set(hand)) == 1

    def is_four_of_a_kind(self, hand):
        return max(hand.count(x) for x in hand) == 4

    def is_full_house(self, hand):
        return len(set(hand)) == 2 and max(hand.count(x) for x in hand) == 3

    def is_three_of_a_kind(self, hand):
        return len(set(hand)) == 3 and max(hand.count(x) for x in hand) == 3

    def is_two_pairs(self, hand):
        return len(set(hand)) == 3 and max(hand.count(x) for x in hand) == 2

    def is_one_pair(self, hand):
        return len(set(hand)) == 4 and max(hand.count(x) for x in hand) == 2

    def is_high_card(self, hand):
        return len(set(hand)) == 5


class Hand:
    def __init__(self, cards: str, bid: int, task: int, camel_cards=CamelCards()):
        self.cards = list(cards)
        self.bid = bid
        self.value = self.calculate_value1(
            camel_cards) if task == 1 else self.calculate_value2(camel_cards)

    def calculate_value1(self, camel_cards):
        value = sum(camel_cards.card_values1[card] * (14 ** (i + 1))
                    for i, card in enumerate(self.cards[::-1]))
        value += camel_cards.get_value_for_highest_type(self.cards)
        return value

    def calculate_value2(self, camel_cards):
        value = sum(camel_cards.card_values2[card] * (14 ** (i + 1))
                    for i, card in enumerate(self.cards[::-1]))
        if "J" in self.cards:
            indexes = [i for i, x in enumerate(self.cards) if x == "J"]
            permutations = [list(x) for x in itertools.product(
                ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"], repeat=len(indexes))]
            hands = []
            for permutation in permutations:
                hand = self.cards.copy()
                for i, index in enumerate(indexes):
                    hand[index] = permutation[i]
                hands.append(hand)
            value += max(camel_cards.get_value_for_highest_type(hand)
                         for hand in hands)
        else:
            value += camel_cards.get_value_for_highest_type(self.cards)
        return value

    def __repr__(self):
        return f"{self.cards} {self.bid}"


with open("2023/day7/input.txt") as f:
    lines = f.readlines()

hands = [Hand(line[0], int(line[1]), 1)
         for line in [line.split() for line in lines]]
hands.sort(key=lambda x: x.value)
print(sum(hand.bid * (i + 1) for i, hand in enumerate(hands)))

hands = [Hand(line[0], int(line[1]), 2)
         for line in [line.split() for line in lines]]
hands.sort(key=lambda x: x.value)
print(sum(hand.bid * (i + 1) for i, hand in enumerate(hands)))
