import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_eq2(self):
        node = TextNode("This is text with a *code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a *code block", TextType.TEXT),
            TextNode(" word", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

    def test_eq3(self):
        node = TextNode("This is text with a *code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        newest_nodes = split_nodes_delimiter(new_nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block",TextType.BOLD),
            TextNode(" word", TextType.CODE),
        ]
        self.assertEqual(newest_nodes, expected)



if __name__ == "__main__":
    unittest.main()