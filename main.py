import random
from suits import is_flush, is_full_house, is_three_of_a_kind, is_straight, is_straight_flush, is_two_pairs, is_four_of_a_kind, is_royal_flush

def main():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [(suit, rank) for suit in suits for rank in ranks]
        return deck

    def calculate_probability(hand_type, num_simulations, suits, ranks):
        hand_count = 0
        for i in range(num_simulations):
            deck = create_deck()
            random.shuffle(deck)
            hand = deck[:5]
            if hand_type == 'flush' and is_flush(hand, suits):
                hand_count += 1
            elif hand_type == 'full house' and is_full_house(hand, suits):
                hand_count += 1
            elif hand_type == 'three of a kind' and is_three_of_a_kind(hand, suits):
                hand_count += 1
            elif hand_type == 'royal flush' and is_royal_flush(hand, suits, ranks):
                hand_count += 1
            elif hand_type == 'straight' and is_straight(hand, suits):
                hand_count += 1
            elif hand_type == 'straight flush' and is_straight_flush(hand, suits):
                hand_count += 1
            elif hand_type == 'two pairs' and is_two_pairs(hand, suits):
                hand_count += 1
            elif hand_type == 'four of a kind' and is_four_of_a_kind(hand, suits):
                hand_count += 1

        probability = hand_count / num_simulations
        print(f'After simulating {num_simulations:,} hands, the probability of getting a {hand_type} is {probability:.2%}.')
        return probability


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

    calculate_probability(hand_type, num_simulations, suits, ranks)

if __name__ == "__main__":
    main()