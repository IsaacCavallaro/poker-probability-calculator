# pylint: disable=missing-module-docstring,missing-function-docstring,consider-using-generator,too-many-function-args
def is_flush(hand):
    suits_in_hand = [card[0] for card in hand]
    return len(set(suits_in_hand)) == 1


def is_full_house(hand):
    values = [card[1] for card in hand]
    return len(set(values)) == 2 and values.count(values[0]) in [2, 3]

def is_three_of_a_kind(hand):
    values = [card[1] for card in hand]
    return len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 3

def is_straight(hand, ranks):
    values = [card[1] for card in hand]
    ranks_values = [ranks.index(value) for value in values]
    sorted_ranks_values = sorted(ranks_values)

    if sorted_ranks_values == [0, 9, 10, 11, 12]:
        # Special case for Ace-10 straight
        return True

    return sorted_ranks_values == list(
        range(sorted_ranks_values[0], sorted_ranks_values[-1] + 1)
    )


def is_straight_flush(hand, ranks):
    return is_straight(hand, ranks) and is_flush(hand)


def is_two_pairs(hand):
    values = [card[1] for card in hand]
    return len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 2

def is_four_of_a_kind(hand):
    values = [card[1] for card in hand]
    return len(set(values)) == 2 and max([values.count(value) for value in set(values)]) == 4

def is_royal_flush(hand):
    values = [card[1] for card in hand]
    return set(values) == set(["Ace", "King", "Queen", "Jack", "10"])
