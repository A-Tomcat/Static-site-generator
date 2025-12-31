import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

#run this to make this executable  --> chmod +x test.sh 
#should be in test.sh already


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("Testing __eq__")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_is_link(self):
        node = TextNode("This is a link node", TextType.LINK)
        self.assertEqual(node.text_type.value, "LINK")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_not_equal_different_type(self):
        node1 = TextNode("same text", TextType.TEXT)
        node2 = TextNode("same text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("some text", TextType.TEXT)
        node2 = TextNode("other text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_equal_with_url(self):
        node1 = TextNode("link text", TextType.LINK, "https://boot.dev")
        node2 = TextNode("link text", TextType.LINK, "https://boot.dev")
        self.assertEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("link text", TextType.LINK, "https://boot.dev")
        node2 = TextNode("link text", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("repr text", TextType.TEXT, "https://boot.dev")
        self.assertEqual("TextNode(repr text, TEXT, https://boot.dev)", repr(node),
    )
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://example.com/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/img.png", "alt": "alt text"},
        )

if __name__ == "__main__":
    unittest.main()