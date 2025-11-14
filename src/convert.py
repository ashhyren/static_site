import re

from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from markdown_blocks import BlockType
from delimiter import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def block_to_tag(block_type, block):
    if block_type is BlockType.PARAGRAPH:
        return "p"
    if block_type is BlockType.HEADING:
        heading_number = len(re.match(r"^(#{1,6})\s+", block).group(1))
        return f"h{heading_number}"
    if block_type is BlockType.CODE:
        return "pre"
    if block_type is BlockType.QUOTE:
        return "blockquote"
    if block_type is BlockType.UNORDERED_LIST:
        return "ul"
    if block_type is BlockType.ORDERED_LIST:
        return "ol"
    else:
        raise ValueError("invalid block type")  
    
def text_to_children(text):
    children_html = []
    children = text_to_textnodes(text)
    for child in children:
        children_html.append(text_node_to_html_node(child))
    return children_html

def block_to_text(block, block_type):
    lines = block.split("\n")
    #Heading
    if block_type is BlockType.HEADING:
        return re.match(r"^(#{1,6}\s+)(.+)",block).group(2).strip()
    #Code
    if block_type is BlockType.CODE:
        clean = []
        for i in range(1,len(lines)-1):
            clean.append(lines[i])
        return "\n".join(clean) + "\n"
    #Quote
    if block_type is BlockType.QUOTE:
        clean = []
        for line in lines:
            clean.append(re.match(r"^(>\s?)(.*)",line).group(2))
        return " ".join(clean)
    #Unordered
    if block_type is BlockType.UNORDERED_LIST:
        clean = []
        for line in lines:
            clean.append(re.match(r"^(-\s?)(.*)", line).group(2))
        return "\n".join(clean)
    #Ordered
    if block_type is BlockType.ORDERED_LIST:
        clean = []
        for line in lines:
            clean.append(re.match(r"^(\d+\.\s?)(.*)", line).group(2))
        return "\n".join(clean)
    if block_type is BlockType.PARAGRAPH:
        clean = []
        for line in lines:
            line = line.strip()
            if line:
                clean.append(line)
        return " ".join(clean)
    else:
        raise ValueError("Improper block_type: text")
    
def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        text = block_to_text(block, block_type)
        child = []
        if block_type is BlockType.ORDERED_LIST or block_type is BlockType.UNORDERED_LIST:
            list_node = []
            lines = text.split("\n")
            for line in lines:
                list_node.append(ParentNode("li",text_to_children(line)))
            child = list_node
        elif block_type is BlockType.CODE:
            code_node = TextNode(text,TextType.TEXT)
            child = [ParentNode("code",[text_node_to_html_node(code_node)])]
        else:
            child = text_to_children(text)
        children.append(ParentNode(block_to_tag(block_type, block),child))
    return ParentNode("div", children)
