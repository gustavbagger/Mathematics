import os
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
    new_content = new_content.replace('href="/',f'href="{basepath}')
    new_content = new_content.replace('src="/',f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path),exist_ok = True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(new_content)
        dest_file.close()
    pass

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for file in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content,file)
        if os.path.isfile(file_path):
            if file[-3:] == ".md":
                file_html = file[:-3]+".html"
                print(file_html)
                dest_path = os.path.join(dest_dir_path,file_html)
                generate_page(file_path,template_path,dest_path,basepath)
            continue
        else:
            dest_path = os.path.join(dest_dir_path,file)
            generate_pages_recursive(file_path,template_path,dest_path,basepath)
            continue
    return
            

    