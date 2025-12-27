#textnode.py
from enum import Enum

# class TextType(Enum):
#     TEXT = "text"
#     BOLD_TEXT = "**Bold Text**"
#     ITALIC_TEXT = "_Italic Text_"
#     CODE_TEXT = "`Code Text`"
#     LINK = "[anchor text](url)"
#     IMAGE = "![alt text](url)"

class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

class TextNode():
    def __init__(self, text, TextType, url = None):
        self.text = text
        self.text_type = TextType
        self.url = url
    def __eq__(self, other):
        A = self.text == other.text
        B = self.text_type == other.text_type
        C = self.url == other.url
        return A and B and C
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
