#!/usr/bin/python3


def islower(c):
    """Check if the character c is lowercase."""
    if ord(c) > 96 and ord(c) < 123:
        return True
    return False
