import re

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) is BlockType.HEADING:
            heading = re.match(r"^(#{1,6})\s+(.+)",block)
            if len(heading.group(1)) == 1:
                return heading.group(2).strip()
        else:
            continue
    raise ValueError("No h1 header")


