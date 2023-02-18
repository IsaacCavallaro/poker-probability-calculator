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
    values.sort(key=lambda x: ranks.index(x))
    if values == ['Ace', '10', 'Jack', 'King', 'Queen']:
        return True
    for i in range(len(values)-1):
        if ranks.index(values[i+1]) - ranks.index(values[i]) != 1:
            return False
    return True

def is_straight_flush(hand, suits, ranks):
    if is_flush(hand, suits) and is_straight(hand, ranks):
        return True
    else:
        return False
    
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
