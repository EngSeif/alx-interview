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
        print(byte[0:1])
        if byte[0:5] == '11110':
            num_bytes = 4
        elif byte[0:4] == '1110':
            num_bytes = 3
        elif byte[0:3] == '110':
            num_bytes = 2
        elif byte[0:2] == '10':
            return False
        elif byte[0:1] == '0':
            i += 1
            continue
        else:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            cont_byte = bin(data[i + j])[2:].zfill(8)
            if cont_byte[:2] != '10':
                return False
        i += num_bytes
    return True
