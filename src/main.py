from textnode import TextNode, TextType
print("hello world")

def main():
    node = TextNode("Link to main Website", TextType.LINK, "https://boot.dev")
    print(node)
    node2 = TextNode("Test text with a **bold word** in the middle.", TextType.TEXT)
    print(node2)
    text_part = node2.text.split("**")
    print(text_part)



main()