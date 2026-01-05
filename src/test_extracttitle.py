#test_extracttitle.py

import unittest
from generate_page import extract_title

class Test_Generate_Page(unittest.TestCase):
    def test_extract_title_first_line(self):
        md = "# My Title\nSome other content"
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_after_blank_line(self):
        md = "\n# Tolkien Fan Club\nMore content"
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_extract_title_strips_whitespace(self):
        md = "#   Spaced Title   \nOther stuff"
        self.assertEqual(extract_title(md), "Spaced Title")

    def test_extract_title_raises_when_no_h1(self):
        md = "## Not an h1\nJust text"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_uses_first_h1(self):
        md = "# First Title\nMore text\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")