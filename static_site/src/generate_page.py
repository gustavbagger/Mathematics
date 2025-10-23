import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown:
        contents_from_path = markdown.read()
        markdown.close()

    with open(template_path) as template:
        contents_template_path = template.read()
        template.close()
    
    print(contents_template_path)
    html_string = markdown_to_html_node(contents_from_path).to_html()
    title = extract_title(contents_from_path)
    new_content = contents_template_path.replace("{{ Title }}",title)
    print(new_content)
    new_content = new_content.replace("{{ Content }}", html_string)
    print(new_content)
    os.makedirs(os.path.dirname(dest_path),exist_ok = True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(new_content)
    pass

    