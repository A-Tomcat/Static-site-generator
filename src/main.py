#main.py
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
from copystatic import move_content
from generate_page import generate_page, generate_pages_recursive
import sys


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    move_content()
    generate_pages_recursive("content", "template.html", "docs", basepath)
    

main()