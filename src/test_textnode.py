import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode
from split_nodes import split_nodes_link, split_nodes_image

#run this to make this executable  --> chmod +x test.sh 
#should be in test.sh already


class TestTextNode(unittest.TestCase):
    def test_eq(self):
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

class Test_MD_TO_TEXTNODE(unittest.TestCase):
    def test_split_simple_code(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(result) == 3
        assert result[0].text == "This is "
        assert result[0].text_type == TextType.TEXT
        assert result[1].text == "code"
        assert result[1].text_type == TextType.CODE
        assert result[2].text == " here"
        assert result[2].text_type == TextType.TEXT


    def test_split_multiple_code_spans(self):
        node = TextNode("`one` and `two`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        texts = [n.text for n in result]
        types = [n.text_type for n in result]
        assert texts == ["one", " and ", "two"]
        assert types == [TextType.CODE, TextType.TEXT, TextType.CODE]


    def test_non_text_nodes_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert result == [node]


    def test_invalid_unclosed_delimiter_raises(self):
        node = TextNode("This is `broken", TextType.TEXT)
        with self.assertRaises(Exception):  # or ValueError if you prefer
            split_nodes_delimiter([node], "`", TextType.CODE)


    def test_split_italic_with_underscore(self):
        node = TextNode("this _word_ works", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        texts = [n.text for n in result]
        types = [n.text_type for n in result]
        assert texts == ["this ", "word", " works"]
        assert types == [TextType.TEXT, TextType.ITALIC, TextType.TEXT]


    def test_empty_sections_skipped(self):
        node = TextNode("`one`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        # no empty text nodes
        for n in result:
            assert n.text != ""

class Test_Split_Nodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )



    pass
if __name__ == "__main__":
    unittest.main()