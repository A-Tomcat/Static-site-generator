#split_nodes.py
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if not node:
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

