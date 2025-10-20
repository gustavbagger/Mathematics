from textnode import TextNode,TextType



def main():
    node = TextNode("this is some anchor text","link","https://www.boot.dev")
    print(node)
    print(node.url)

main()