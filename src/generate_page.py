import os
import shutil

from markdown_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown:
        contents_from_path = markdown.read()
        markdown.close()

    with open(template_path) as template:
        contents_template_path = template.read()
        template.close()

    html_string = markdown_to_html_node(contents_from_path).to_html()
    title = extract_title(contents_from_path)
    new_content = contents_template_path.replace("{{ Title }}",title)

    new_content = new_content.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path),exist_ok = True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(new_content)
        dest_file.close()
    pass

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    for file in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content,file)
        dest_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(file_path):
            if file.endswith(".md"):
                dest_path = os.path.join(dest_dir_path,file[:-3]+".html")
                generate_page(file_path,template_path,dest_path,basepath)
            
            elif file.lower().endswith(".pdf"):
                shutil.copy2(file_path,dest_path)

        elif os.path.isdir(file_path):
            dest_path = os.path.join(dest_dir_path,file)
            generate_pages_recursive(file_path,template_path,dest_path,basepath)
            
    return
            

    