#!/usr/bin/python3

"""
pascal_triangle :
    A Module that contain function to calculate pascal triangle to a
    certain row number entered by the user
"""


def pascal_triangle(n):
    """
    pascal_triangle :
    A function to calculate pascal triangle to a
    certain row number entered by the user
    """
    pascalTriangle = []
    if n <= 0:
        return []
    for i in range(0, n):
        if i == 0:
            pascalTriangle.append([1])
        elif i == 1:
            pascalTriangle.append([1, 1])
        else:
            appendedRow = []
            k = 0
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    appendedRow.append(1)
                else:
                    appendedRow.append(
                        pascalTriangle[i-1][k] +
                        pascalTriangle[i-1][k + 1]
                    )
                    k = k + 1
            pascalTriangle.append(appendedRow)
    return pascalTriangle
