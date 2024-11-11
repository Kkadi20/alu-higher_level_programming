#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    # Open the file using the `with` statement to ensure it closes automatically
    with open(filename, encoding="utf-8") as file:
        # Read and print the file's content
        print(file.read(), end="")
