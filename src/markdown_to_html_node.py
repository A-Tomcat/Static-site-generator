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
                lines = block.split("\n")
                text = " ".join(lines)
                text_nodes = text_to_textnode(text)
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

'''Main function:

    markdown_to_html_node(markdown) - The entry point

Helper functions:

    block_to_html_node(block) - Routes each block to the appropriate handler
    text_to_children(text) - Shared function that converts text with inline markdown to a list of HTML children
    paragraph_to_html_node(block) - Handles paragraphs
    heading_to_html_node(block) - Handles headings
    code_to_html_node(block) - Handles code blocks
    olist_to_html_node(block) - Handles ordered lists
    ulist_to_html_node(block) - Handles unordered lists
    quote_to_html_node(block) - Handles quotes

    Key differences from your approach:

    Separate function for each block type - Instead of one big match statement, each block type gets its own function. This makes the code more modular and easier to test.

    block_to_html_node router - This acts as a dispatcher that determines the block type and calls the appropriate function. Much cleaner than a giant match statement!

    text_to_children shared helper - This is brilliant! Instead of repeating the "convert text nodes to HTML nodes" logic in every block type, it's extracted into one reusable function. Notice how almost every block type uses it (except code blocks).

    Better error handling - Functions like heading_to_html_node and code_to_html_node validate their input and raise meaningful errors.

Your approach vs the solution:

    Yours: One big function with a match statement - everything in one place
    Solution: Multiple small, focused functions - easier to read, test, and maintain

Both work! But as projects grow, the modular approach becomes much easier to manage. Great question - understanding different ways to structure code is super valuable!
'''