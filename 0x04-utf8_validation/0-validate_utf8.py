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
        # Determine the number of bytes in the current UTF-8 character
        byte = data[i]
        if byte >> 7 == 0:          # 1-byte character (0xxxxxxx)
            num_bytes = 1
        elif byte >> 5 == 0b110:    # 2-byte character (110xxxxx)
            num_bytes = 2
        elif byte >> 4 == 0b1110:   # 3-byte character (1110xxxx)
            num_bytes = 3
        elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
            num_bytes = 4
        else:                       # Invalid starting byte
            return False

        # Check if there are enough bytes remaining for this character
        if i + num_bytes > len(data):
            return False

        # Validate each continuation byte (must start with '10')
        for j in range(1, num_bytes):
            if data[i + j] >> 6 != 0b10:
                return False

        # Move to the next character in the data
        i += num_bytes

    return True
