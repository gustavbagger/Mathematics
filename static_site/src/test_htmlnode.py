import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", children = [HTMLNode()]).props_to_html()
        expected = ''
        self.assertEqual(node,expected)

    def test_one_prop(self):
        node = HTMLNode("p", props = {"hey":"there"}).props_to_html()
        expected = ' hey="there"'
        self.assertEqual(node,expected)

    def test_no_props(self):
        node = HTMLNode("p", children = [HTMLNode()], props = {"hey":"there","another":"pair"}).props_to_html()
        expected = ' hey="there" another="pair"'
        self.assertEqual(node,expected) 

if __name__ == "__main__":
    unittest.main()
