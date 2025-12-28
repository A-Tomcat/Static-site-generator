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
        present = ""
        for prop in self.props:
            present += f'"{prop}": "{self.props[prop]}" '
        return f'''{self.props}'''
    

    def __repr__(self):
        pass