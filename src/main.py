from textnode import TextNode, TextType
print("hello world")

def main():
    node = TextNode("Link to main Website", TextType.LINK, "https://boot.dev")
    print(node)



main()