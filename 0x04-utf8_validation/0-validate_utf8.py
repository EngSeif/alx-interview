#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    validate if a set of data
    is a valid utf-8 code
    """
    def countOnes(num):
        """
        Get number of leading ones
        """
        mask = 1 << 7
        i = 0
        while num & mask:
            i += 1
            mask = mask >> 1
        return i
    count = 0
    for d in data:
        if count == 0:
            count = countOnes(d)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if countOnes(d) != 1:
                return False
    return count == 0
