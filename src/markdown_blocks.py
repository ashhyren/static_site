def markdown_to_blocks(markdown):
    block = []
    block_unedited = markdown.split('\n\n')
    for blocks in block_unedited:
        if blocks == "":
            continue
        block.append(blocks.strip())
    return block