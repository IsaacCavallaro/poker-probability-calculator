def is_flush(hand, suits):
    suits_in_hand = [card[0] for card in hand]
    if len(set(suits_in_hand)) == 1:
        return True
    else:
        return False
    
def is_full_house(hand, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 2 and values.count(values[0]) in [2, 3]:
        return True
    else:
        return False
    
def is_three_of_a_kind(hand, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 3:
        return True
    else:
        return False
    
def is_straight(hand, ranks):
    values = [card[1] for card in hand]
    ranks_values = [ranks.index(value) for value in values]
    sorted_ranks_values = sorted(ranks_values)
    
    if sorted_ranks_values == [0, 9, 10, 11, 12]:
        # Special case for Ace-10 straight
        return True
    
    return sorted_ranks_values == list(range(sorted_ranks_values[0], sorted_ranks_values[-1] + 1))


def is_straight_flush(hand, suits, ranks):
    return is_straight(hand, ranks) and is_flush(hand, suits)

    
def is_two_pairs(hand, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 2:
        return True
    else:
        return False
    
def is_four_of_a_kind(hand, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 2 and max([values.count(value) for value in set(values)]) == 4:
        return True
    else:
        return False
    
def is_royal_flush(hand, suits, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 5 and set(values) == set(['Ace', 'King', 'Queen', 'Jack', '10']):
        return True
    else:
        return False
