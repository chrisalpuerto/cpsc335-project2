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