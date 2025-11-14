import os

from convert import markdown_to_html_node
from extract import extract_title
from copystatic import copy

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as path:
        markdown_str = path.read()
    with open(template_path) as template:
        template_str = template.read()
    html = markdown_to_html_node(markdown_str).to_html()
    title = extract_title(markdown_str)
    template_str = template_str.replace("{{ Title }}", title)
    template_str = template_str.replace("{{ Content }}", html)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir) and dest_dir != "":
        os.makedirs(dest_dir)
    with open(dest_path,mode="w") as dest:
        dest.write(template_str)

    