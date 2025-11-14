from copystatic import copy_refresh
from generate import generate_pages_recursive

static = "static"
public = "public"
template = "template.html"
content = "content"

def main():
    copy_refresh(static,public)
    generate_pages_recursive(content, template, public)

main()

