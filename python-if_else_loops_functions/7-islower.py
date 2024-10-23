#!/usr/bin/python3

def islower(c):
    """Check if the character c is lowercase."""
    if ord(c) > 96 and ord(c) < 123:
        return True
    return False

if __name__ == "__main__":
    # Test cases
    test_chars = ['a', 'H', 'g', '3', 'A']
    for char in test_chars:
        print("{} is {}".format(char, "lower" if islower(char) else "upper"))

