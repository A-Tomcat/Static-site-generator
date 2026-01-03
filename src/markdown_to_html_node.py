#markdown_to_html_node.py

from textnode import *
from htmlnode import *
from text_to_textnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                tag = "p"
                text_nodes = text_to_textnode(block)
                html_nodes = []
                for text_node in text_nodes:
                    html_nodes.append(text_node_to_html_node(text_node))
                paragraph_node = ParentNode(tag, html_nodes)
                block_nodes.append(paragraph_node)

            case BlockType.HEADING:
                count = 0
                for ch in block:
                    if ch == "#":
                        count += 1
                    else: break
                heading_text = block[count + 1:]
                tag = f"h{count}"
                text_nodes = text_to_textnode(heading_text)
                html_nodes = []
                for text_node in text_nodes:
                    html_nodes.append(text_node_to_html_node(text_node))
                heading_node = ParentNode(tag, html_nodes)
                block_nodes.append(heading_node)


            case BlockType.QUOTE:
                tag = "blockquote"
                html_nodes = []
                quote_lines = block.split("\n")
                text = ""
                for line in quote_lines:
                    line = line.lstrip(">").strip()
                    if text != "":
                        text = text + " " + line
                    else: text = line
                nodes = text_to_textnode(text)
                for node in nodes:
                    html_nodes.append(text_node_to_html_node(node))
                quote_node = ParentNode(tag, html_nodes)
                block_nodes.append(quote_node)

            case BlockType.CODE:
                tag = "code"
                nested_tag = "pre"
                content = block[4:-3]
                node = TextNode(content, TextType.TEXT)
                leaf_node = text_node_to_html_node(node)
                code_node = ParentNode(tag, [leaf_node])
                pre_node = ParentNode(nested_tag, [code_node])
                block_nodes.append(pre_node)

            case BlockType.UNORDERED_LIST:
                tag = "ul"
                nested_tag = "li"
                html_nodes = []
                lines = block.split("\n")
                for line in lines:
                    new_line = line[2:]
                    nested_nodes = []
                    nodes = text_to_textnode(new_line)
                    for node in nodes:
                        nested_nodes.append(text_node_to_html_node(node))
                    html_nodes.append(ParentNode(nested_tag, nested_nodes))
                tag_node = ParentNode(tag, html_nodes)
                block_nodes.append(tag_node)
                
                
            case BlockType.ORDERED_LIST:
                tag = "ol"
                nested_tag = "li"
                html_nodes = []
                lines = block.split("\n")
                for line in lines:
                    dot_index = line.index(".")
                    new_line = line[dot_index + 2:]
                    nested_nodes = []
                    nodes = text_to_textnode(new_line)
                    for node in nodes:
                        nested_nodes.append(text_node_to_html_node(node))
                    html_nodes.append(ParentNode(nested_tag, nested_nodes))
                tag_node = ParentNode(tag, html_nodes)
                block_nodes.append(tag_node)

            case _:
                raise TypeError(f"BlockType does not exist!")
        #HTMLNode(tag, value, children, props)
    return ParentNode("div", block_nodes)