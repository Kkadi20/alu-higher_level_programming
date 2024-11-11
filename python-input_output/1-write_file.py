#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

"""
    # Open the file in write mode using `with` to ensure automatic closure
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file and return the character count
        return file.write(text)

