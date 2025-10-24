import unittest

from textnode import TextNode, TextType
from aux_functions import extract_markdown_images, extract_markdown_links
from aux_functions import split_nodes_image, split_nodes_link, split_nodes_delimiter
from aux_functions import text_to_textnodes, markdown_to_blocks


class TestExtracts(unittest.TestCase):

    def test_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_links(self):
        matches = extract_markdown_links(
        "This is text with a [link text](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link text", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_image_is_not_link(self):
        matches = extract_markdown_links(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)  
    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
            )   

    def test_split_links(self):
        node = TextNode(
        "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
            )   
            
    def test_split_links_with_image(self):
        node = TextNode(
        "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an ![image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and an ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
            )  

    def test_split_links_and_images(self):
        node = TextNode(
        "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an ![image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image(split_nodes_link([node]))
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,"https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
            )    


    def test_markdown_to_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text)
        )

    def test_markdown_close(self):
        text = "This is **bold**_italic_and normal `ish` text."
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("and normal ", TextType.TEXT),
                TextNode("ish", TextType.CODE),
                TextNode(" text.", TextType.TEXT),
            ],
            text_to_textnodes(text)
        )
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



if __name__ == "__main__":
    unittest.main()