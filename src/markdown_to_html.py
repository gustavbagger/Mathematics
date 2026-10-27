
from htmlnode import HTMLNode, ParentNode, LeafNode
from aux_functions import markdown_to_blocks, text_to_textnodes
from blocktype import block_to_block_type, BlockType
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    markdown_body = "\n".join(markdown.splitlines()[1:])
    list_of_blocks = markdown_to_blocks(markdown_body)
    block_list = list()
    under_h1 = False
    under_h3 = False

    for block in list_of_blocks:
        block_type = block_to_block_type(block)
        if under_h1:
            section_props = {"class": "under_h1"} 
        elif under_h3:
            section_props = {"class": "under_h3"}
        else: 
            section_props = None
        match block_type:

            case BlockType.MULTI_COLUMN:
            
                columns = []
                current_column = None

                for raw_line in block.splitlines():
                    line = raw_line.strip()
                    if line == "mul":
                        current_column = []
                        columns.append(current_column)
                        continue

                    if line.startswith("mul "):
                        current_column = []
                        columns.append(current_column)
                        line = line[4:].strip()

                    if not line:
                        continue

                    if current_column is None:
                        raise ValueError("Multi-column block must start with mul")

                    if line.startswith("#### "):
                        tag = "h4"
                        text = line[5:].strip()
                    else:
                        tag = "p"
                        text = line
                    
                    children = [
                        text_node_to_html_node(node)
                        for node in text_to_textnodes(text)
                    ]

                    current_column.append(
                            ParentNode(
                                tag=tag,
                                children=children,
                                props= section_props
                            )
                        )

                column_nodes = [
                    ParentNode(
                        tag="div",
                        children=column,
                        props={"class":"multi-column-item"},
                    )
                    for column in columns
                ]

                block_node = ParentNode(
                    tag="div",
                    children=column_nodes,
                    props={
                        "class": "multi-column",
                        "style": f"--column-count: {len(columns)};",
                           },
                    )
                                        

            case BlockType.PARAGRAPH:
                tag = "p"
                text_nodes = text_to_textnodes(block)
                children = list()

                for node in text_nodes:

                    children.append(text_node_to_html_node(node))


                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=section_props)

            case BlockType.HEADING:
                count = 0
                max_check = min(len(block),6)
                while count < max_check and block[count] == "#":
                    count += 1

                under_h3 = (count == 3)
                under_h1 = (count == 1)

                tag = f"h{count}"
                block = block[count:].strip()

                text_nodes = text_to_textnodes(block)
                children = list()
                for node in text_nodes:
                    children.append(text_node_to_html_node(node))

                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=None)

            case BlockType.UNLIST:
                tag = "ul"
                tag_child = "li"

                block_lines = block.split("\n")
                children = list()
                for line in block_lines:
                    line = line[2:]
                    line_text_nodes = text_to_textnodes(line)
                    line_children = list()
                    for node in line_text_nodes:
                        line_children.append(text_node_to_html_node(node))
                    line_parent = ParentNode(tag = tag_child, children = line_children) 
                    children.append(line_parent)
                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=section_props)


            case BlockType.LIST:
                tag_child = "li"
                
                block_lines = block.split("\n")
                if block_lines[0].startswith(".1 "):
                    tag = "ol reversed"
                else:
                    tag = "ol"
                children = list()
                for line in block_lines:
                    line = line[3:]
                    line_text_nodes = text_to_textnodes(line)
                    line_children = list()
                    for node in line_text_nodes:
                        line_children.append(text_node_to_html_node(node))
                    line_parent = ParentNode(tag = tag_child, children = line_children) 
                    children.append(line_parent)
                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=section_props)

            case BlockType.QUOTE:
                tag = "blockquote"
                block = block.replace("> ","")
                text_nodes = text_to_textnodes(block)
                children = list()
                for node in text_nodes:
                    children.append(text_node_to_html_node(node))

                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=section_props)              

            case BlockType.CODE:
                tag = "code"
                block = block[3:-3]
                if block.split("\n")[0] == "":
                    block = block[1:]
                text_node = TextNode(block,TextType.CODE)
                tag = "pre"
                children = [text_node_to_html_node(text_node)]
                block_node = ParentNode(tag = tag, 
                                        children = children,
                                        props=section_props)
        block_list.append(block_node)

    return ParentNode(tag = "div", children = block_list)
            