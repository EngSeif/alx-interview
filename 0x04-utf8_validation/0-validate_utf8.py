#!/usr/bin/python3
"""
Validate UTF-8 Data
"""

def validUTF8(data):
    remaining = 0
    for code in data:
        if remaining == 0:
            if code >> 7 == 0b0:
                remaining = 0
            elif code >> 5 == 0b110:
                remaining = 1
            elif code >> 4 == 0b1110:
                remaining = 2
            elif code >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if (code >> 6 == 0b10):
                remaining -= 1
            else:
                return False
    if remaining == 0:
        return True
    else:
        return False
