#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file with the given filename.

    Parameters:
    - filename (str): The name of the file to be written.
    - text (str): The text content to be written to the file.

    Returns:
    - int: The number of characters written to the file.

    Raises:
    - IOError: If there is an issue with opening or writing to the file.
    """

    with open(filename, "w") as file_obj:
        return file_obj.write(text)
