import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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



    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h(self):
        node = LeafNode("h", "Hello, world!")
        self.assertEqual(node.to_html(), "<h>Hello, world!</h>")

    def test_leaf_to_html_link(self):
        node = LeafNode("h", "Hello, world!",props = {"href":'boot.dev'})
        self.assertEqual(node.to_html(), '<h href="boot.dev">Hello, world!</h>')



    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_several_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()
