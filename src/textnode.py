from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "**Bold Text**"
    ITALIC_TEXT = "_Italic Text_"
    CODE_TEXT = "`Code Text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, TextType, url = None):
        self.text = text
        self.text_type = TextType
        self.url = url
    
    def __eq__(self, Node):
        return super().__eq__(Node)
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
