import re
from .pac import Pac


def zzz():
    return "Zzz..."


def block_text(file_name, head):
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
