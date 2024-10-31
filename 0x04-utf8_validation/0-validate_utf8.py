#!/usr/bin/python3
"""
Validate UTF-8 Data
"""


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding.
    """
    if len(data) == 0:
        return False
    i = 0
    while i < len(data):
        byte = bin(data[i])[2:].zfill(8)
        # Determine how many bytes are expected based on the leading bits
        if byte.startswith('11110'):
            num_bytes = 4
        elif byte.startswith('1110'):
            num_bytes = 3
        elif byte.startswith('110'):
            num_bytes = 2
        elif byte.startswith('10'):
            return False  # A continuation byte cannot start with '10'
        elif byte.startswith('0'):
            num_bytes = 1
        else:
            return False  # Invalid starting byte

        # Check if we have enough bytes left
        if i + num_bytes > len(data):
            return False

        # Validate continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data):
                return False  # Not enough bytes remaining
            cont_byte = bin(data[i + j])[2:].zfill(8)
            if not cont_byte.startswith('10'):
                return False  # Invalid continuation byte

        i += num_bytes

    return True
