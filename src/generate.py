import os

from convert import markdown_to_html_node
from extract import extract_title
from copystatic import copy

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as path:
        markdown_str = path.read()
    with open(template_path) as template:
        template_str = template.read()
    html = markdown_to_html_node(markdown_str).to_html()
    title = extract_title(markdown_str)
    template_str = template_str.replace("{{ Title }}", title)
    template_str = template_str.replace("{{ Content }}", html)
    template_str = template_str.replace('href="/',f'href="{basepath}')
    template_str = template_str.replace('src="/',f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir) and dest_dir != "":
        os.makedirs(dest_dir)
    with open(dest_path,mode="w") as dest:
        dest.write(template_str)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        if os.path.isfile(src_path) and item.endswith(".md"):
            generate_page(src_path, template_path, os.path.join(dest_dir_path,item[0:-3]+".html"), basepath)
        elif os.path.isdir(src_path):
            dest_dir = os.path.join(dest_dir_path, item)
            os.mkdir(dest_dir)
            generate_pages_recursive(src_path, template_path, dest_dir, basepath)
        else:
            continue