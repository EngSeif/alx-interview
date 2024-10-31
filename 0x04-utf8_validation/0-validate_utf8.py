#!/usr/bin/python3
"""
Validate UTF-8 Data
"""


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        byte = bin(data[i])[2:].zfill(8)
        if byte.startswith('11110'):
            num_bytes = 4
        elif byte.startswith('1110'):
            num_bytes = 3
        elif byte.startswith('110'):
            num_bytes = 2
        elif byte.startswith('0'):
            num_bytes = 1
        else:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            cont_byte = ''
            if i + j >= len(data):
                return False
            else:
                cont_byte = bin(data[i + j])[2:].zfill(8)
            if not cont_byte.startswith('10'):
                return False
        i += num_bytes
    return True
