
from htmlnode import HTMLNode, ParentNode, LeafNode
from aux_functions import markdown_to_blocks, text_to_textnodes
from blocktype import block_to_block_type, BlockType
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown)
    block_list = list()
    for block in list_of_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                tag = "p"
                
                text_nodes = text_to_textnodes(block)
                children = list()
                for node in text_nodes:
                    node.text = node.text.replace("\n"," ")
                    children.append(text_node_to_html_node(node))

                block_node = ParentNode(tag = tag, children = children)

            case BlockType.HEADING:
                count = 0
                max_check = min(len(block),6)
                while count < max_check and block[count] == "#":
                    count += 1
                tag = f"h{count}"

                text_nodes = text_to_textnodes(block)
                children = list()
                for node in text_nodes:
                    children.append(text_node_to_html_node(node))

                block_node = ParentNode(tag = tag, children = children)

            case BlockType.UNLIST:
                tag = "ul"
                tag_child = "li"

                block_lines = block.split("\n")
                children = list()
                for line in block_lines:
                    line_text_nodes = text_to_textnodes(line)
                    line_children = list()
                    for node in line_text_nodes:
                        line_children.append(text_node_to_html_node(node))
                    line_parent = ParentNode(tag = tag_child, children = line_children) 
                    children.append(line_parent)
                block_node = ParentNode(tag = tag, children = children)


            case BlockType.LIST:
                tag = "ol"
                tag_child = "li"

                block_lines = block.split("\n")
                children = list()
                for line in block_lines:
                    line_text_nodes = text_to_textnodes(line)
                    line_children = list()
                    for node in line_text_nodes:
                        line_children.append(text_node_to_html_node(node))
                    line_parent = ParentNode(tag = tag_child, children = line_children) 
                    children.append(line_parent)
                block_node = ParentNode(tag = tag, children = children)

            case BlockType.QUOTE:
                tag = "blockquote"
                text_nodes = text_to_textnodes(block)
                children = list()
                for node in text_nodes:
                    children.append(text_node_to_html_node(node))

                block_node = ParentNode(tag = tag, children = children)               

            case BlockType.CODE:
                tag = "code"
                text_node = TextNode(block[3:-3],TextType.CODE)
                
                block_node = ParentNode(tag = "pre", children = [text_node_to_html_node(text_node)])
            
        block_list.append(block_node)

    return ParentNode(tag = "div", children = block_list)
            