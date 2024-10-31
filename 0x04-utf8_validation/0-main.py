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

def tests():
    assert validUTF8([0]) == True
    assert validUTF8([127]) == True
    assert validUTF8([65]) == True  # 'A'
    assert validUTF8([192, 169]) == True  # '©' (U+00A9)
    assert validUTF8([226, 130, 172]) == True  # '€' (U+20AC)
    assert validUTF8([228, 184, 150]) == True  # '汉' (U+6C49)
    assert validUTF8([240, 159, 152, 128]) == True  # '😐' (U+1F612)

    # Invalid UTF-8 test cases
    assert validUTF8([255]) == False
    assert validUTF8([128]) == False
    assert validUTF8([240, 162, 138, 128, 145]) == False
    assert validUTF8([230, 136, 145, 145]) == False
    assert validUTF8([192, 168, 240]) == False

    # Insufficient bytes for multi-byte characters
    assert validUTF8([235, 140]) == False
    assert validUTF8([224, 164]) == False

    # Leading continuation byte without a valid preceding byte
    assert validUTF8([240, 159, 146]) == False

    # Edge cases
    assert validUTF8([]) == True
    assert validUTF8([240, 159, 146, 150, 128]) == False
    # Case with incomplete multi-byte character
    assert validUTF8([240, 159, 146]) == False  # Valid start but missing continuation byte

    print("All tests passed!")

tests()
