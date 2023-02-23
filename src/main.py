# pylint: disable=missing-module-docstring,missing-function-docstring,too-many-function-args
import random
from src.suits import (
    is_flush,
    is_full_house,
    is_three_of_a_kind,
    is_straight,
    is_straight_flush,
    is_two_pairs,
    is_four_of_a_kind,
    is_royal_flush,
)


def create_deck(suits, ranks):
    deck = [(suit, rank) for suit in suits for rank in ranks]
    return deck


def calculate_probability(hand_type, num_simulations, suits, ranks):
    # pylint: disable=unused-variable
    hand_count = 0
    for i in range(num_simulations):
        deck = create_deck(suits, ranks)
        random.shuffle(deck)
        hand = deck[:5]
        if hand_type == "flush" and is_flush(hand, suits):
            hand_count += 1
        elif hand_type == "full house" and is_full_house(hand, suits):
            hand_count += 1
        elif hand_type == "three of a kind" and is_three_of_a_kind(
            hand, suits
        ):
            hand_count += 1
        elif hand_type == "royal flush" and is_royal_flush(hand, suits, ranks):
            hand_count += 1
        elif hand_type == "straight" and is_straight(hand, ranks):
            hand_count += 1
        elif hand_type == "straight flush" and is_straight_flush(
            hand, suits, ranks
        ):
            hand_count += 1
        elif hand_type == "two pairs" and is_two_pairs(hand, suits):
            hand_count += 1
        elif hand_type == "four of a kind" and is_four_of_a_kind(hand, suits):
            hand_count += 1

    if hand_count == 0:
        probability = 0
        expected_frequency = float("inf")
    else:
        probability = hand_count / num_simulations
        expected_frequency = int(1 / probability)

    print(
        f"After simulating {num_simulations:,} hands," 
        f"the probability of getting a {hand_type} is {probability:.2%}, "
        f"which means that out of every {expected_frequency:,} hands played, "
        f"you can expect to get a {hand_type} about"
        f"{num_simulations // expected_frequency:,} times."
    )
    return probability

def main():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    hand_types = [
        "flush",
        "full house",
        "three of a kind",
        "straight",
        "straight flush",
        "two pairs",
        "four of a kind",
        "royal flush",
    ]

    print("Select a hand type:")
    for i, hand_type in enumerate(hand_types):
        print(f"{i+1}. {hand_type}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            hand_type = hand_types[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

    while True:
        try:
            num_simulations = int(input("Enter the number of simulations: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    calculate_probability(hand_type, num_simulations, suits, ranks)


if __name__ == "__main__":
    main()
