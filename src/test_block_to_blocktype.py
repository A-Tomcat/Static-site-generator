from text_to_textnode import block_to_block_type, BlockType
import unittest
class Test_block_to_block_type(unittest.TestCase):
    def test_code_block(self):
        block = "```Print('Hello World')```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)