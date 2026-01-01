#split_nodes.py
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        delimiter = extract_markdown_images(text)

        if not delimiter:
            new_nodes.append(node)
            continue

        for alt, url in delimiter:
            before, after = text.split(f"![{alt}]({url})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        delimiter = extract_markdown_links(text)

        if not delimiter:
            new_nodes.append(node)
            continue

        for link, url in delimiter:
            before, after = text.split(f"[{link}]({url})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(link, TextType.LINK, url))

            text = after
            
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


#split nodes as reference:
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             new_nodes.append(node)
#             continue

#         text_part = node.text.split(delimiter)

#         if len(text_part) % 2 == 0:
#             raise Exception(f"Invalid Markdown Syntax!")
#         for i in range(0, len(text_part)):
#             if text_part[i] == "":
#                 continue
#             if i % 2 == 0:
#                 new_nodes.append(TextNode(text_part[i], TextType.TEXT))
#             else:
#                 new_nodes.append(TextNode(text_part[i], text_type))
#     return new_nodes
