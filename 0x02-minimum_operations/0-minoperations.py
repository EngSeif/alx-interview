#!/usr/bin/python3
"""
MinOperations :
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
        -   Copy All and Paste.
    Given a number n, write a method that calculates the
    fewest number of operations needed to
    result in exactly n H characters in the file.

    -   Prototype: def minOperations(n)
    -   Returns an integer
    -   If n is impossible to achieve, return 0
"""
from math import sqrt


def isPrime(n: int) -> bool:
    """
    isPrime(n):
    Check if the number is prime or not
    """
    if (n <= 1):
        return False
    elif (n == 2 or n == 3):
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        for i in range(5, int(sqrt(n)) + 1, 6):
            if (n % i == 0):
                return False
    return True


def minOperations(n):
    """
    minOperations:
    Calc least number of operation (Copy all and paste)
    to have n chars of H
    """
    if n <= 1 or isPrime(n):
        return 0
    nOperation = 0
    for i in range(2, n + 1):
        while n % i == 0:
            nOperation += i
            n //= i
    return nOperation
