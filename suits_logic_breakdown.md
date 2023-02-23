# Suits Logic Breakdown

## `is_flush(hand, suits)`

```python
def is_flush(hand, suits):
    suits_in_hand = [card[0] for card in hand]
    if len(set(suits_in_hand)) == 1:
        return True
    else:
        return False
```

This function takes:
 - hand 
    - list of five cards 
- suits 
    - list of possible suits


- It creates a new list `suits_in_hand` containing the first element (the suit) of each card in the hand
- If there is only one unique suit in the hand (i.e., if the length of the set of `suits_in_hand` is 1), then the function returns True, indicating that the hand is a flush 
- Otherwise, the function returns False.

---

## `is_full_house(hand, ranks)`

```python
def is_full_house(hand, ranks):
    values = [card[1] for card in hand]
    if len(set(values)) == 2 and values.count(values[0]) in [2, 3]:
        return True
    else:
        return False
```

This function takes:
 - hand 
    - list of five cards 
- ranks 
    - list of all possible ranks

-  It creates a new list `values` containing the second element (the rank) of each card in the hand
- If there are only two unique ranks in the hand (i.e., if the length of the set of values is 2), and one of those ranks appears either two or three times in the hand (i.e., if the count of the first rank in values is either 2 or 3), then the function returns True, indicating that the hand is a full house
- Otherwise, the function returns False

---