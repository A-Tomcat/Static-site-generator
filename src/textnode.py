#textnode.py
from enum import Enum
from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

class TextNode:
    def __init__(self, text, Text_Type, url = None):
        self.text = text
        self.text_type = Text_Type
        self.url = url
    def __eq__(self, other):
        A = self.text == other.text
        B = self.text_type == other.text_type
        C = self.url == other.url
        return A and B and C
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
    
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
            
        case TextType.CODE:
            return LeafNode("code", text_node.text)

        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception(f"TextType not valid!")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node is not TextType.TEXT:
            new_nodes.append(node)
            continue
        match delimiter:
            case "**":
                pass
