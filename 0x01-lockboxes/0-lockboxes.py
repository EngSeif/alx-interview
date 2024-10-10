#!/usr/bin/python3

"""
Lockboxes :
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    canUnlockAll :
    a method that determines if all the boxes can be opened.
    """
    keys = set(boxes[0])
    opened = set()
    closed = set(range(1, len(boxes)))
    while closed:
        found = False
        for box in list(closed):
            if box in keys:
                found = True
                opened.add(box)
                closed.remove(box)
                keys.update(boxes[box])
        if not found:
            break
    return len(closed) == 0
