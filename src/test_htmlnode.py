import unittest

from htmlnode import HTMLNode
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