#htmlnode.py

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        pass


    def to_html(self):
        raise NotImplemented
    

    def props_to_html(self):
        if not self.props:
            return ""
        attributes = [f'{key}="{value}"' for key, value in self.props.items()]
        return " ".join(attributes)
        # join attributes with a single space between each

    def __repr__(self):
        return f'''HTMLNode:\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}'''
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value!")
        #if no tag: just raw text
        if self.tag == None:
            return str(self.value)
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag!")
        
        if not self.children:
            raise ValueError("ParentNode must have children!")
        html = ""
        for child in self.children:
            html += child.to_html()
        html = f'''<{self.tag}{self.props_to_html()}>{html}</{self.tag}>'''
        return html