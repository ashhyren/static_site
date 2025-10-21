import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT and delimiter is not None:
            split = node.text.split(delimiter)
            if len(split) % 2 == 0:
                raise ValueError("invalid markdown: missing closing delimiter")
            for i in range(0,len(split)):
                if split[i] == "":
                    continue
                if i % 2 != 0:
                    new_nodes.append(TextNode(split[i], text_type))
                else:
                    new_nodes.append(TextNode(split[i], TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) > 0:
            image_alt, image_link = images[0]
            section = node.text.split(f"![{image_alt}]({image_link})",1)
            if len(section) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if section[1] != "":
                section_node = [TextNode(section[1], TextType.TEXT)]
                new_nodes.extend(split_nodes_image(section_node))
        else:
                new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) > 0:
            link_alt, link_link = links[0]
            section = node.text.split(f"[{link_alt}]({link_link})",1)
            if len(section) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_link))
            if section[1] != "":
                section_node = [TextNode(section[1], TextType.TEXT)]
                new_nodes.extend(split_nodes_link(section_node))
        else:
                new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    text_node = [TextNode(text,TextType.TEXT)]
    text_node = split_nodes_delimiter(text_node,"**",TextType.BOLD)
    text_node = split_nodes_delimiter(text_node,"_",TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node,"`",TextType.CODE)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    return text_node

