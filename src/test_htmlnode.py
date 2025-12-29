import unittest

from htmlnode import HTMLNode, LeafNode
#run this to make this executable  --> chmod +x test.sh 
#should be in test.sh already

class Test_HTMLNode(unittest.TestCase):
    def test_no_input(self):
        print("Testing __init__ with no input:")
        node = HTMLNode()
        a = False
        if node.children == None:
            if node.props == None:
                if node.tag == None:
                    if node. value == None:
                        a = True
        print(f"All 4 data members are None: {a}")
        self.assertEqual(a, True)
    
    def test_leaf_to_html_p(self):
        print('''Testing LeafNode: "p", "Hello, world!"''')
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_raw_text_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_with_props_a_tag(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        html = node.to_html()
        # Order of attributes can matter, so assert on an exact expected string
        self.assertEqual(
            html,
            '<a href="https://www.google.com" target="_blank">Click me!</a>',
        )

    def test_leaf_raises_when_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_props_to_html_empty(self):
        node = LeafNode("p", "hi", None)
        self.assertEqual(node.props_to_html(), "")