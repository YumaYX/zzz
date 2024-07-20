import re
from .pac import Pac


def zzz():
    """
    Returns a string representing the sound of sleeping.

    Returns:
        str: The sound "Zzz..."
    """
    return "Zzz..."


def block_text(file_name, head):
    """
    Reads a file and divides its content into blocks based on a specified heading.

    Args:
        file_name (str): The name of the file to read.
        head (str): The heading pattern to identify the start of a new block.

    Returns:
        list: A list of Pac objects, each representing a block of text.
    """
    blocks = []

    with open(file_name, "r") as file:
        current_block = None

        for line in file:
            line = line.strip()

            if re.search(head, line):
                current_block = Pac(line)
                blocks.append(current_block)
            elif current_block is not None:
                current_block.push(line)

    return blocks
