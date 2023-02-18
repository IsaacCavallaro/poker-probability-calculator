import random
from suits import is_flush, is_full_house, is_three_of_a_kind, is_straight, is_straight_flush, is_two_pairs, is_four_of_a_kind, is_royal_flush


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(suit, rank) for suit in suits for rank in ranks]


def test_is_flush():
    hand = [('Hearts', 'Ace'), ('Hearts', '5'), ('Hearts', '7'), ('Hearts', '10'), ('Hearts', 'King')]
    assert is_flush(hand, suits) == True


def test_is_full_house():
    hand = [('Hearts', 'Ace'), ('Diamonds', 'Ace'), ('Clubs', 'Ace'), ('Hearts', 'King'), ('Diamonds', 'King')]
    assert is_full_house(hand, ranks) == True


def test_is_three_of_a_kind():
    hand = [('Hearts', 'Ace'), ('Diamonds', 'Ace'), ('Clubs', 'Ace'), ('Hearts', 'King'), ('Diamonds', '10')]
    assert is_three_of_a_kind(hand, ranks) == True


def test_is_straight():
    hand = [('Hearts', 'Ace'), ('Diamonds', '10'), ('Clubs', 'Jack'), ('Hearts', 'Queen'), ('Diamonds', 'King')]
    assert is_straight(hand, ranks) == True


def test_is_straight_flush():
    hand = [('Hearts', 'Ace'), ('Hearts', '2'), ('Hearts', '3'), ('Hearts', '4'), ('Hearts', '5')]
    assert is_straight_flush(hand, suits, ranks) == True


def test_is_two_pairs():
    hand = [('Hearts', 'Ace'), ('Diamonds', 'Ace'), ('Clubs', 'King'), ('Hearts', 'King'), ('Diamonds', '10')]
    assert is_two_pairs(hand, ranks) == True


def test_is_four_of_a_kind():
    hand = [('Hearts', 'Ace'), ('Diamonds', 'Ace'), ('Clubs', 'Ace'), ('Spades', 'Ace'), ('Diamonds', '10')]
    assert is_four_of_a_kind(hand, ranks) == True


def test_is_royal_flush():
    hand = [('Hearts', 'Ace'), ('Hearts', 'King'), ('Hearts', 'Queen'), ('Hearts', 'Jack'), ('Hearts', '10')]
    assert is_royal_flush(hand, suits, ranks) == True

