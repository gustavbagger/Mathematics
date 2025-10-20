from textnode import TextNode,TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(self):
   match self.text_type:
    case TextType.TEXT:
        return LeafNode(tag = None, value = self.text)
    case TextType.BOLD:
        return LeafNode(tag = "b", value = self.text)
    case TextType.ITALIC:
        return LeafNode(tag = "i", value = self.text)
    case TextType.CODE:
        return LeafNode(tag = "code", value = self.text)  
    case TextType.LINK:
        return LeafNode(tag = "a", value = self.text,props = {"href":self.url})  
    case TextType.IMAGE:
        return LeafNode(tag = "img", value = "", props ={"src":self.url,"alt":self.text})           
    case _:
        raise Exception("Error: invalid text type")