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

