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
        byte = data[i]
        
        # Determine the number of bytes to expect
        if byte >> 5 == 0b110:  # 2-byte character
            num_bytes = 2
        elif byte >> 4 == 0b1110:  # 3-byte character
            num_bytes = 3
        elif byte >> 3 == 0b11110:  # 4-byte character
            num_bytes = 4
        elif byte >> 7 == 0:  # 1-byte character
            num_bytes = 1
        else:
            return False
        
        # Check if there are enough bytes left in data
        if i + num_bytes > len(data):
            return False
        
        # Validate continuation bytes
        for j in range(1, num_bytes):
            if (data[i + j] >> 6) != 0b10:  # Check for 10xxxxxx
                return False

        i += num_bytes

    return True
