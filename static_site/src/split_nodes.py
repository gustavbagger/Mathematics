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
