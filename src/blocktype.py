import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered_list"
    LIST = "ordered_list"
    MULTI_COLUMN = "multi_column"

def block_to_block_type(block):
    block_lines = [line.strip() for line in block.splitlines()]
    
    mul_count = sum(
    line.startswith("mul ")
    for line in block_lines
    )

    if (
        block_lines[0].startswith("mul ")
        and mul_count >= 2
    ):
        return BlockType.MULTI_COLUMN
    
    if (
        len(block_lines) >= 2
        and all(line.startswith("mul ") for line in block_lines)
    ):
        return BlockType.MULTI_COLUMN

    
    if len(re.findall(r"^#{1,6} ",block))!= 0:
        return BlockType.HEADING

    if len(re.findall(r"^`{3}",block_lines[0]))!=0 and len(re.findall(r"`{3}$",block_lines[-1]))!=0:
        return BlockType.CODE

    switch = [True,True,True]
    line_nr = 1
    for line in block_lines:
        if switch[0] and line.startswith(">"):
            switch[1] = False
            switch[2] = False
            continue
        if switch[1] and line.startswith("- "):
            switch[0] = False
            switch[2] = False
            continue
        if switch[2] and (line.startswith(f"{line_nr}. ") or line.startswith(f"{line_nr}) ") or line.startswith("1) ") or line.startswith("1. ") or line.startswith(".1 ")):
            switch[0] = False
            switch[1] = False
            line_nr += 1
            continue
        return BlockType.PARAGRAPH
    
    return BlockType.QUOTE if switch[0] else BlockType.UNLIST if switch[1] else BlockType.LIST




