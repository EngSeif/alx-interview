#!/usr/bin/python3
"""
Validate UTF-8 Data
"""

def validUTF8(data):
    i = 0
    while i < len(data):
        byte = data[i] & 0xFF

        # Check if the byte is within valid byte range (0-255)
        if data[i] < 0 or data[i] > 255:
            return False

        # Determine the number of bytes to expect based on the leading byte
        if (byte >> 5) == 0b110:  # 2-byte character
            num_bytes = 2
        elif (byte >> 4) == 0b1110:  # 3-byte character
            num_bytes = 3
        elif (byte >> 3) == 0b11110:  # 4-byte character
            num_bytes = 4
        elif (byte >> 7) == 0:  # 1-byte character
            num_bytes = 1
        else:
            return False  # Invalid leading byte

        # Check if there are enough bytes left in data
        if i + num_bytes > len(data):
            return False

        # Validate continuation bytes
        for j in range(1, num_bytes):
            con_bit = data[i + j] & 0xFF
            if (con_bit  >> 6) != 0b10: 
                return False
        i += num_bytes

    return True
