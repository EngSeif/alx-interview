#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

data = [0, 0, 0, 0]
print(validUTF8(data))
print(validUTF8([]))
print('--------')
print(validUTF8([467, 133, 108]))
print(validUTF8([240, 188, 128, 167]))
print(validUTF8([235, 140]))
print(validUTF8([345, 467]))
print(validUTF8([192, 145]))


test_cases = [
    ([197, 130, 1], True),       # Valid UTF-8
    ([235, 140, 4], False),      # Invalid UTF-8
    ([240, 162, 138, 147], True), # Valid UTF-8
    ([248, 130, 130, 130], False), # Invalid UTF-8
    ([255], False),               # Invalid byte
    ([0, 0, 0], True),            # Multiple 1-byte characters
    ([192, 145], False),          # Invalid continuation
    ([226, 130, 172], True),      # Valid 3-byte character
    ([128], False),               # Invalid single continuation byte
    ([237, 160, 128, 1], False),  # Invalid 4-byte character
]

# Testing
for idx, (data, expected) in enumerate(test_cases):
    result = validUTF8(data)
    assert result == expected, f"Test case {idx + 1} failed: {data}, expected {expected}, got {result}"

print("All test cases passed!")