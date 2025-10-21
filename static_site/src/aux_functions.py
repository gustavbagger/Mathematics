import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    return_list = list()
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            return_list.append(node)
            continue
        node_list = node.text.split(delimiter)
        even = 0
        for new_value in node_list:
            if even == 0:
                return_list.append(TextNode(new_value,TextType.TEXT))
            else:
                return_list.append(TextNode(new_value,text_type))
            even = (even + 1) % 2
    return return_list

def split_nodes_image(old_nodes):
    return_list = list()
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            return_list.append(node)
            continue  
        images_list = extract_markdown_images(node.text)
        if len(images_list)==0:
            return_list.append(node)
            continue
        current_node = node
        node_list = list()
        for image in images_list:
            delimiter = f"![{image[0]}]({image[1]})"
            node_list = current_node.text.split(delimiter)
            return_list.append(TextNode(node_list[0], TextType.TEXT))  
            return_list.append(TextNode(image[0], TextType.IMAGE, url =image[1]))
            if node_list[1] != "":
                current_node = TextNode(node_list[1],TextType.TEXT)
                continue
            break
        if len(node_list)>1 and node_list[1] != "":
            return_list.append(current_node)
    return return_list
        
def split_nodes_link(old_nodes):
    return_list = list()
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            return_list.append(node)
            continue  
        links_list = extract_markdown_links(node.text)
        if len(links_list)==0:
            return_list.append(node)
            continue
        current_node = node
        node_list = list()
        for link in links_list:
            delimiter = f"[{link[0]}]({link[1]})"
            node_list = current_node.text.split(delimiter)
            return_list.append(TextNode(node_list[0], TextType.TEXT))  
            return_list.append(TextNode(link[0], TextType.LINK, url = link[1]))
            if node_list[1] != "":
                current_node = TextNode(node_list[1],TextType.TEXT)
                continue
            break
        if len(node_list)>1 and node_list[1] != "":
            return_list.append(current_node)
    return return_list


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)