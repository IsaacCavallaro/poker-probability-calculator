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

