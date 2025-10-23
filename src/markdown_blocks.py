import re

from enum import Enum

def markdown_to_blocks(markdown):
    block = []
    block_unedited = markdown.split('\n\n')
    for blocks in block_unedited:
        if blocks == "":
            continue
        block.append(blocks.strip())
    return block

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    lines = markdown.split("\n")
    #Heading
    if re.match(r"^#{1,6}\s",lines[0]):
        return BlockType.HEADING
    #Code
    if len(lines) > 1 and re.match(r"^```$",lines[0]) and re.match(r"^```$",lines[-1]):
        return BlockType.CODE
    #Quote
    for line in lines:
        if not re.match(r"^>", line):
            break
    else:
        return BlockType.QUOTE
    #Unordered
    for line in lines:
        if not re.match(r"^- ", line):
            break
    else:
        return BlockType.UNORDERED_LIST
    #Ordered
    i = 1
    for line in lines:
        if not re.match(rf"^{i}\. ", line):
            break
        i += 1
    else:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    