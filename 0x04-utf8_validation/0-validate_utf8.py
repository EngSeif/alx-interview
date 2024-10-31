#!/usr/bin/python3
"""

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
            i += 1
            for j in range(i, i + 1):
                num = bin(data[i])[2:].zfill(8)
                if num[:2] != '10':
                    return False
            i += 1
        elif binany_num[:4] == '1110':
            i += 1
            for j in range(i, i + 2):
                num = bin(data[j])[2:].zfill(8)
                if num[:2] != '10':
                    return False
            i += 2
        elif binany_num[:5] == '11110':
            i += 1
            for j in range(i, i + 3):
                num = bin(data[j])[2:].zfill(8)
                if num[:2] != '10':
                    return False
            i += 3
    return True
