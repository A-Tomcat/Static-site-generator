import unittest

from textnode import TextNode, TextType

#run this to make this executable  --> chmod +x test.sh 
#should be in test.sh already


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("Testing __eq__")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_islink(self):
        node = TextNode("This is a link node", TextType.LINK)
        self.assertEqual(node.text_type.value, "LINK")



if __name__ == "__main__":
    unittest.main()