#main.py
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
from copystatic import move_content
from generate_page import generate_page, generate_pages_recursive
import sys


def main():
    output_dir = "docs"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    move_content("static", output_dir)
    generate_pages_recursive("content", "template.html", output_dir, basepath)
    

main()