#text_to_textnode.py
from textnode import TextNode, TextType, BlockType, split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnode(text):
    node = split_nodes_image([TextNode(text, TextType.TEXT)])
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    return node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            new_blocks.append((stripped))
    return new_blocks


def is_ordered_list_block(block: str):
    lines = block.split("\n")
    expected = 1
    for line in lines:
        parts = line.split(". ", 1)
        if len(parts) != 2:
            return False
        number_str, _ = parts
        if not number_str.isdigit():
            return False
        if int(number_str) != expected:
            return False
        expected += 1
    return True

def block_to_block_type(block):
    if block.startswith("#"):
        counter = 0
        for i in range (0, 7):
            if block[i] and block[i] == "#":
                counter += 1
            else:
                break
        if 1 <= counter <= 6 and len(block) > counter and block[counter] == " ":
            return BlockType.HEADING
        

    match block:
        case s if s.startswith("```") and s.endswith("```"):
            return BlockType.CODE
        
        case s if all(line.startswith(">") for line in s.split("\n")):
            return BlockType.QUOTE
        
        case s if all(line.startswith("- ") for line in s.split("\n")):
            return BlockType.UNORDERED_LIST
        
        case s if is_ordered_list_block(s):
            return BlockType.ORDERED_LIST
        
        case _:
            return BlockType.PARAGRAPH

        