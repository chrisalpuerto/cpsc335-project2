# Algorithm 2: Vibe Check - Card Shuffle
# Author: Jonathan Quiroz
# CSUF Email: jquiroz44@csu.fullerton.edu
# Submission: Project 2

from collections import Counter
from typing import List


def canArrange(hand: List[int], groupSize: int) -> bool:
    # If the total number of cards isn't divisible by groupSize, we cannot form valid groups
    if len(hand) % groupSize != 0:
        return False

    card_count = Counter(hand)

    # Process the cards in sorted order
    for card in sorted(card_count):
        if card_count[card] > 0:  # If there are cards to process
            count = card_count[card]

            # Try to form a valid group starting from the current card
            for i in range(groupSize):
                if card_count[card + i] < count:  
                    return False
                card_count[card + i] -= count  
    return True


# Efficiency Analysis:
# The algorithm sorts the cards (O(N log N)) and then iterates over them, making the overall complexity O(N log N).
# Using a Counter to keep track of frequencies makes the card lookup and modification O(1) per operation.


# Example
if __name__ == '__main__':
    hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize1 = 3
    print(canArrange(hand1, groupSize1))  # Expected Output: True

    hand2 = [1, 2, 3, 3, 4, 5, 6, 7]
    groupSize2 = 4
    print(canArrange(hand2, groupSize2))  # Expected Output: False
