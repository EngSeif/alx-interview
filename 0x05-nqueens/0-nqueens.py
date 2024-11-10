#!/usr/bin/python3
"""
Solving N-Queens Problem
"""

import sys


def Solve(N: int):
    """
    Contains The main logic to solve
    The problem
    """
    cols = set()
    posDiag = set()
    negDiag = set()
    result = []
    board = []

    def backTrack(r):
        """
        Do BackTracking
        """
        if r == N:
            result.append([x for x in board])
            return

        for c in range(N):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                continue
            cols.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board.append([r, c])

            backTrack(r + 1)

            cols.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.remove([r, c])

    backTrack(0)
    return result


def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)
    result = Solve(N)
    for Row in result:
        print(Row)


main()
