#text_to_textnode.py
from textnode import TextNode, TextType, split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnode(text):
    node_images = split_nodes_image([TextNode(text, TextType.TEXT)])
    node_links = split_nodes_link(node_images)
    node_code = split_nodes_delimiter(node_links, "`", TextType.CODE)
    node_bold = split_nodes_delimiter(node_code, "**", TextType.BOLD)
    node_result = split_nodes_delimiter(node_bold, "_", TextType.ITALIC)
    return node_result