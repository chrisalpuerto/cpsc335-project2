## CPSC 335 Project 2

Algorithm 1 by Chris, Algorithm 2 by Jonathan

## ALGORITHM 1: 
# Overview

In a world where Titans have breached the Walls of Maria, humanity must seek refuge in the remaining safe strongholds. This algorithm computes the shortest distance from every open city area to the nearest safe zone, navigating around impassable Titan-infested areas.

The solution updates the grid **in-place** using a **multi-source Breadth-First Search (BFS)** to simulate the spread of safety across the city.

---

## Problem Description

You're given an `m x n` 2D grid representing a city where each cell can be:

- `-1`: Titan-infested area (impassable)
- `0`: Safe stronghold
- `INF`: Open city area (humans trying to survive)

**Goal**: Update all `INF` cells with the shortest distance to the nearest safe stronghold (`0`). If unreachable, it should remain `INF`.

---

## Input Format

A 2D grid (list of lists) of size `m x n` with:

- `-1` representing Titan zones  
- `0` representing safe strongholds  
- `INF` (INF as a string in this implementation) representing open areas  

---

## Output Format

- The grid is **updated in-place** with shortest distances from open city areas to the nearest stronghold.
- Unreachable areas remain `INF`.

---

## Constraints

- `1 ≤ m, n ≤ 250`
- At least one `0` exists in the grid
- Only 4-directional movement allowed (up, down, left, right)

---

## Algorithm

This problem is solved using **multi-source BFS**:

1. Enqueue all strongholds (`0`s) as starting points.
2. Use BFS to explore all `INF` cells.
3. Update each `INF` with its shortest distance from the nearest stronghold.
4. Avoid blocked cells (`-1`) and out-of-bound positions.

---

## Algorithm 2: Vibe Check - Card Shuffle 🃏🔥

### Problem Description

Before starting a card game, the deck needs to be organized into valid groups.  
You are given a list of integers `hand`, where each element represents a card, and an integer `groupSize`, which defines how many cards should be in each group.

Each group must satisfy the following:
- The group contains exactly `groupSize` cards.
- The cards in a group must be consecutive in value (increasing by 1 each time).

Your task is to determine whether the entire deck can be rearranged into valid groups. If it can, return `True`; otherwise, return `False`.

---

### Input Format

- `hand`: A list of integers (1 ≤ len(hand) ≤ 10^5)
- `groupSize`: An integer (1 ≤ groupSize ≤ len(hand))

---

### Output Format

- Return `True` if the deck can be perfectly grouped as per the rules.
- Return `False` otherwise.

---
## How to Solve It

To determine whether the hand of cards can be rearranged into valid groups, we use a greedy algorithm combined with a frequency counter.

### Step-by-Step Approach:

1. **Check divisibility**:  
   If the total number of cards in `hand` is not divisible by `groupSize`, it is impossible to create groups of equal size, so return `False`.

2. **Count occurrences**:  
   Use `collections.Counter` to count how many times each card appears.

3. **Sort the hand**:  
   Sort the unique card values in ascending order. This allows us to always try forming groups starting from the smallest available card.

4. **Form groups greedily**:  
   For each card in the sorted order:
   - If the card's count is greater than 0, attempt to create a group of size `groupSize` starting from this card.
   - Check the next `groupSize - 1` consecutive cards to ensure each has at least the same count.
   - Subtract the count from all cards in the group.
   - If at any point a required card is missing or doesn’t have enough copies, return `False`.

5. **Return `True`** if all cards are successfully grouped.

### Why This Works:

- Sorting ensures we always process the smallest possible sequences first.
- The greedy method ensures we never skip lower values that would make it impossible to complete valid groups later.
- The counter efficiently tracks how many of each card are left as we form groups.

This solution is efficient and can handle large inputs due to the linear nature of the counting and the limited number of passes through the data.
### How to Run

```bash
python3 algo1.py
python3 Algorithm 2 Vibe Check.py
```