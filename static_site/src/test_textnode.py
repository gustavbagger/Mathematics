import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("test", TextType.ITALIC, None)
        node2 = TextNode("test", TextType.ITALIC)
        self.assertEqual(node,node2)
    
    def test_dif_text_type(self):
        node = TextNode("test", TextType.ITALIC)
        node2 = TextNode("test", TextType.BOLD)
        self.assertNotEqual(node,node2)   

    def test_dif_text(self):     
        node = TextNode("testing", TextType.ITALIC)
        node2 = TextNode("test", TextType.ITALIC)
        self.assertNotEqual(node,node2)   

if __name__ == "__main__":
    unittest.main()