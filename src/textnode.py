from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "**Bold Text**"
    ITALIC_TEXT = "_Italic Text_"
    CODE_TEXT = "`Code Text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode(Enum):
    def __init__(self, text, TextType, url = None):
        self.text = text
        self.text_type = TextType
        self.url = url
    
    def __eq__(self, Node):
        if self.text == Node.text and self.text_type == Node.TextType and self.url == Node.url:
            return True
        
    def __repr__(self):
        return f"{self}({self.text}, {self.text_type}, {self.url})"