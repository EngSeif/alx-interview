#!/usr/bin/python3
"""
Validate UTF-8 Data
"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        binany_num = bin(data[i])[2:].zfill(8)
        if binany_num[0] == '0':
            i += 1
            continue
        elif binany_num[:3] == '110':
            num_bytes = 2
        elif binany_num[:4] == '1110':
            num_bytes = 3
        elif binany_num[:5] == '11110':
            num_bytes = 4
        else:
            return False

        if i + num_bytes >= len(data):
            return False

        for j in range(1, num_bytes):
            binany_num = bin(data[i + j])[2:].zfill(8)
            if binany_num[:2] != '10':
                return False
        i += num_bytes
    return True
