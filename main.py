import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(suit, rank) for suit in suits for rank in ranks]

def is_flush(hand):
    suits = [card[0] for card in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False
    
def is_full_house(hand):
    values = [card[1] for card in hand]
    if len(set(values)) == 2 and values.count(values[0]) in [2, 3]:
        return True
    else:
        return False
    
def is_three_of_a_kind(hand):
    values = [card[1] for card in hand]
    if len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 3:
        return True
    else:
        return False
    
def is_straight(hand):
    values = [card[1] for card in hand]
    values.sort(key=lambda x: ranks.index(x))
    if values == ['Ace', '10', 'Jack', 'King', 'Queen']:
        return True
    for i in range(len(values)-1):
        if ranks.index(values[i+1]) - ranks.index(values[i]) != 1:
            return False
    return True

def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False
    
def is_two_pairs(hand):
    values = [card[1] for card in hand]
    if len(set(values)) == 3 and max([values.count(value) for value in set(values)]) == 2:
        return True
    else:
        return False
    
def is_four_of_a_kind(hand):
    values = [card[1] for card in hand]
    if len(set(values)) == 2 and max([values.count(value) for value in set(values)]) == 4:
        return True
    else:
        return False
    
def is_royal_flush(hand):
    values = [card[1] for card in hand]
    if len(set(values)) == 5 and set(values) == set(['Ace', 'King', 'Queen', 'Jack', '10']):
        return True
    else:
        return False

def calculate_probability(hand_type, num_simulations):
    hand_count = 0
    for i in range(num_simulations):
        random.shuffle(deck)
        hand = deck[:5]
        if hand_type == 'flush' and is_flush(hand):
            hand_count += 1
        elif hand_type == 'full house' and is_full_house(hand):
            hand_count += 1
        elif hand_type == 'three of a kind' and is_three_of_a_kind(hand):
            hand_count += 1
        elif hand_type == 'royal flush' and is_royal_flush(hand):
            hand_count += 1
        elif hand_type == 'straight' and is_straight(hand):
            hand_count += 1
        elif hand_type == 'straight flush' and is_straight_flush(hand):
            hand_count += 1
        elif hand_type == 'two pairs' and is_two_pairs(hand):
            hand_count += 1
        elif hand_type == 'four of a kind' and is_four_of_a_kind(hand):
            hand_count += 1

    probability = hand_count / num_simulations
    print(probability)



while True:
    hand_type = input('Enter the hand type (flush, full house, three of a kind, royal flush): ')
    if hand_type not in ['flush', 'full house', 'three of a kind', 'royal flush']:
        print('Invalid input. Please try again.')
    else:
        break

while True:
    try:
        num_simulations = int(input('Enter the number of simulations: '))
        break
    except ValueError:
        print('Invalid input. Please enter an integer.')

calculate_probability(hand_type, num_simulations)