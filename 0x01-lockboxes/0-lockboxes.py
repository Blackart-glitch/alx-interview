#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set()
    unlocked.add(0)  # Start with the first box (index 0) unlocked

    for box_index in unlocked:
        for key in boxes[box_index]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)

    return len(unlocked) == n
