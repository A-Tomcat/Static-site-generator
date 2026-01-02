from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
print("hello world")

def main():
    # node = TextNode("Link to main Website", TextType.LINK, "https://boot.dev")
    # print(node)
    # node2 = TextNode("Test text with a **bold word** in the middle.", TextType.TEXT)
    # print(node2)
    # text_part = node2.text.split("**")
    # print(text_part)
    node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)
    result = text_to_textnode(node.text)
    for n in result:
        print(n)


main()